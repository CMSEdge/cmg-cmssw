from CMGTools.TTHAnalysis.treeReAnalyzer import *

class edgeFriends:
    def __init__(self,label,tightLeptonSel,cleanJet,isMC=True):
        self.label = "" if (label in ["",None]) else ("_"+label)
        self.tightLeptonSel = tightLeptonSel
        self.cleanJet = cleanJet
        self.isMC = isMC
        self.puFile = open("/afs/cern.ch/work/m/mdunser/public/puWeighting/puWeights.txt","r")
        self.pu_dict = eval(self.puFile.read())
        self.puFile.close()
    def listBranches(self):
        label = self.label
        biglist = [ ("nLepTight"+label, "I"), ("nJetSel"+label, "I"), ("nPairLep"+label, "I"),
                 ("iLT"+label,"I",20,"nLepTight"+label), 
                 ("iJ"+label,"I",20,"nJetSel"+label), # index >= 0 if in Jet; -1-index (<0) if in DiscJet
                 ("nLepGood20"+label, "I"), ("nLepGood20T"+label, "I"),
                 ("nJet35"+label, "I"), ("htJet35j"+label), ("nBJetLoose35"+label, "I"), ("nBJetMedium35"+label, "I"), 
                 ("iL1T"+label, "I"), ("iL2T"+label, "I"), 
                 ("lepsMll"+label, "F"), ("lepsJZB"+label, "F"), ("lepsDR"+label, "F"), ("lepsMETRec"+label, "F"), ("lepsZPt"+label, "F"),
                 ("Lep1_pt"+label, "F"), ("Lep1_eta"+label, "F"), ("Lep1_phi"+label, "F"), ("Lep1_miniRelIso"+label, "F"), ("Lep1_pdgId"+label, "I"), ("Lep1_mvaIdPhys14"+label, "F"),
                 ("Lep2_pt"+label, "F"), ("Lep2_eta"+label, "F"), ("Lep2_phi"+label, "F"), ("Lep2_miniRelIso"+label, "F"), ("Lep2_pdgId"+label, "I"), ("Lep2_mvaIdPhys14"+label, "F"),
                 ("PileupW"+label, "F"),
                 ("min_mlb1"+label, "F"),
                 ("min_mlb2"+label, "F")
                 ]
        ## for lfloat in 'pt eta phi miniRelIso pdgId'.split():
        ##     if lfloat == 'pdgId':
        ##         biglist.append( ("Lep"+label+"_"+lfloat,"I", 10, "nPairLep"+label) )
        ##     else:
        ##         biglist.append( ("Lep"+label+"_"+lfloat,"F", 10, "nPairLep"+label) )
        for jfloat in "pt eta phi mass btagCSV rawPt".split():
            biglist.append( ("JetSel"+label+"_"+jfloat,"F",20,"nJetSel"+label) )
        if self.isMC:
            biglist.append( ("JetSel"+label+"_mcPt",     "F",20,"nJetSel"+label) )
            biglist.append( ("JetSel"+label+"_mcFlavour","I",20,"nJetSel"+label) )
            biglist.append( ("JetSel"+label+"_mcMatchId","I",20,"nJetSel"+label) )
        return biglist
    def __call__(self,event):
        leps  = [l for l in Collection(event,"LepGood","nLepGood")]
        lepso = [l for l in Collection(event,"LepOther","nLepOther")]
        jetsc = [j for j in Collection(event,"Jet","nJet")]
        jetsd = [j for j in Collection(event,"DiscJet","nDiscJet")]
        (met, metphi)  = event.met_pt, event.met_phi
        ##ntrue = event.nTrueInt
        nvtx = event.nVert
        metp4 = ROOT.TLorentzVector()
        metp4.SetPtEtaPhiM(met,0,metphi,0)
        ret = {}; jetret = {}; 
        lepret = {}
        
        #
        ### Define tight leptons
        ret["iLT"] = []; ret["nLepGood20T"] = 0

        # ====================
        # do pileupReweighting
        # ====================
        puWt = self.pu_dict[nvtx] if self.isMC else 1.
        if puWt > 3: puWt = 3.
        ret["PileupW"] = puWt

        # ===============================
        # new, simpler sorting of leptons
        # ===============================
        for il,lep in enumerate(leps):
            clean = True
            if self.tightLeptonSel(lep) and clean:
                ret["iLT"].append(il)
                if lep.pt > 20: ret["nLepGood20T"] += 1
        # other leptons, negative indices
        for il,lep in enumerate(lepso):
            clean = True
            if self.tightLeptonSel(lep) and clean:
                ret["iLT"].append(-1-il)
                if lep.pt > 20: ret["nLepGood20T"] += 1
        ret["nLepTight"] = len(ret["iLT"])
        #
        # sort the leptons by pT:
        ret["iLT"].sort(key = lambda idx : leps[idx].pt if idx >= 0 else lepso[-1-idx].pt, reverse = True)

        ## search for the lepton pair
        #lepst  = [ leps [il] for il in ret["iLT"] ]

        lepst = []
        for il in ret['iLT']:
            if il >=0: 
                lepst.append(leps[il])
            else: 
                lepst.append(lepso[-1-il])
        #

        iL1iL2 = self.getPairVariables(lepst, metp4)
        ret['iL1T'] = ret["iLT"][ iL1iL2[0] ] if (len(ret["iLT"]) >=1 and iL1iL2[0] != -999) else -999
        ret['iL2T'] = ret["iLT"][ iL1iL2[1] ] if (len(ret["iLT"]) >=2 and iL1iL2[1] != -999) else -999
        ret['lepsMll'] = iL1iL2[2] 
        ret['lepsJZB'] = iL1iL2[3] 
        ret['lepsDR'] = iL1iL2[4] 
        ret['lepsMETRec'] = iL1iL2[5] 
        ret['lepsZPt'] = iL1iL2[6] 

        #print 'new event =================================================='
        l1 = ROOT.TLorentzVector()
        l2 = ROOT.TLorentzVector()
        ltlvs = [l1, l2]
        for lfloat in 'pt eta phi miniRelIso pdgId mvaIdPhys14'.split():
            if lfloat == 'pdgId':
                lepret["Lep1_"+lfloat+self.label] = -99
                lepret["Lep2_"+lfloat+self.label] = -99
            else:
                lepret["Lep1_"+lfloat+self.label] = -42.
                lepret["Lep2_"+lfloat+self.label] = -42.
        if ret['iL1T'] != -999 and ret['iL2T'] != -999:
            ret['nPairLep'] = 2
#            print 'index of lepton 1 %d index of lepton 2 %d' %( ret['iL1T'], ret['iL2T'])
            ## for lfloat in 'pt eta phi miniRelIso pdgId'.split():
            ##     lepret["Lep1_"+lfloat+label] = -42.
            ##     lepret["Lep2_"+lfloat+label] = -42.
            # compute the variables for the two leptons in the pair
            lcount = 1
            for idx in [ret['iL1T'], ret['iL2T']]:
                lep = leps[idx] if idx >= 0 else lepso[-1-idx]
                #for lfloat in 'pt eta phi miniRelIso pdgId'.split():
                #    lepret[lfloat].append( getattr(lep,lfloat) )
                for lfloat in 'pt eta phi miniRelIso pdgId mvaIdPhys14'.split():
                    lepret["Lep"+str(lcount)+"_"+lfloat+self.label] = getattr(lep,lfloat)
                ltlvs[lcount-1].SetPtEtaPhiM(lep.pt, lep.eta, lep.phi, 0.0005 if lep.pdgId == 11 else 0.106)
                lcount += 1
                #print 'good lepton', getattr(lep,'pt'), getattr(lep,'eta'), getattr(lep,'phi'), getattr(lep,'pdgId') 
        else:
            ret['nPairLep'] = 0
            
        ### Define jets
        ret["iJ"] = []
        # 0. mark each jet as clean
        for j in jetsc+jetsd: j._clean = True
        # set _clean flag of bad jets to False
        for j in jetsc+jetsd:
            if abs(j.eta) > 2.4 or j.pt < 35:
                j._clean = False
                continue
            for l in lepst:
                #lep = leps[l]
                if deltaR(l,j) < 0.4:
                    j._clean = False

        # 2. compute the jet list
        
        for ijc,j in enumerate(jetsc):
            if not j._clean: continue
            ret["iJ"].append(ijc)
        for ijd,j in enumerate(jetsd):
            if not j._clean: continue
            ret["iJ"].append(-1-ijd)
        ret['nJetSel'] = len(ret["iJ"])

        # 3. sort the jets by pt
        
        ret["iJ"].sort(key = lambda idx : jetsc[idx].pt if idx >= 0 else jetsd[-1-idx].pt, reverse = True)

        # 4. compute the variables
        
        for jfloat in "pt eta phi mass btagCSV rawPt".split():
            jetret[jfloat] = []
        if self.isMC:
            for jmc in "mcPt mcFlavour mcMatchId".split():
                jetret[jmc] = []
        for idx in ret["iJ"]:
            jet = jetsc[idx] if idx >= 0 else jetsd[-1-idx]
            for jfloat in "pt eta phi mass btagCSV rawPt".split():
                jetret[jfloat].append( getattr(jet,jfloat) )
            if self.isMC:
                for jmc in "mcPt mcFlavour mcMatchId".split():
                    jetret[jmc].append( getattr(jet,jmc) )
        
        # 5. compute the sums
        
        ret["nJet35"] = 0; ret["htJet35j"] = 0; ret["nBJetLoose35"] = 0; ret["nBJetMedium35"] = 0
        for j in jetsc+jetsd:
            if not j._clean: continue
            ret["nJet35"] += 1; ret["htJet35j"] += j.pt; 
            if j.btagCSV>0.423: ret["nBJetLoose35"] += 1
            if j.btagCSV>0.814: ret["nBJetMedium35"] += 1
        ## compute mlb for the two lepton  
        jet = ROOT.TLorentzVector()	
        min_mlq1 = 1e6
        min_mlq2 = 1e6
        lepindex, jetindex = -999, -999
        paired_with_b = False
        for j in jetsc+jetsd:
            if ret["nJetSel"] < 1: continue
            if ret['nPairLep'] < 2: continue
            if not j._clean: continue
            jet.SetPtEtaPhiM(j.pt, j.eta, j.phi, j.mass)           
            tmp = (l1+jet).M()  
            if j.btagCSV>0.814:  
                if tmp < min_mlq1: 
                     min_mlq1  = tmp
                     paired_with_b = True 
                     jetindex = j 
            else:
                 if tmp < min_mlq1 and paired_with_b == False:
                     min_mlq1 = tmp 
        for j in jetsc+jetsd: 
            if ret["nPairLep"] < 2: continue
            if ret["nJetSel"] < 1: continue
            if not j._clean: continue
            jet.SetPtEtaPhiM(j.pt, j.eta, j.phi, j.mass)           
            tmp = (l2+jet).M()
            if j.btagCSV>0.814:  
                if tmp < min_mlq2: 
                    min_mlq2  = tmp
                    paired_with_b = True    
            else:
                if tmp < min_mlq2 and paired_with_b == False:
                    min_mlq2 = tmp            
        ret["min_mlb1"] = min(min_mlq1,min_mlq2) if min(min_mlq1, min_mlq2) < 1e6 else -1.
        ret["min_mlb2"] = max(min_mlq1,min_mlq2) if max(min_mlq1, min_mlq2) < 1e6 else -1.
       ### attach labels and return
        fullret = {}
        for k,v in ret.iteritems(): 
            fullret[k+self.label] = v
        for k,v in jetret.iteritems(): 
            fullret["JetSel%s_%s" % (self.label,k)] = v
        #for k,v in lepret.iteritems(): 
        #    fullret["Lep%s_%s" % (self.label,k)] = v
        for k,v in lepret.iteritems(): 
            fullret[k] = v
        return fullret

    def getMll_JZB(self, l1, l2, met):
        metrecoil = (met + l1 + l2).Pt()
        zpt = (l1 + l2).Pt()
        jzb = metrecoil - zpt
        return (l1+l2).M(), jzb, l1.DeltaR(l2), metrecoil, zpt

    def getPairVariables(self,lepst, metp4):
        ret = (-999,-999,-99., 0., -99., -99., -99.)
        if len(lepst) >= 2:
            [mll, jzb, dr, metrec, zpt] = self.getMll_JZB(lepst[0].p4(), lepst[1].p4(), metp4)
            ret = (0, 1, mll, jzb, dr, metrec, zpt)
        return ret


def _susyEdge(lep):
        if lep.pt <= 10.: return False
        if abs(lep.eta) > 2.4: return False
        if abs(lep.dxy) > 0.05: return False
        if abs(lep.dz ) > 0.10: return False
        if abs(lep.eta) > 1.4 and abs(lep.eta) < 1.6: return False
        # marc aug07 if abs(lep.pdgId) == 13 and lep.muonMediumId != 1: return False
        if abs(lep.pdgId) == 13 and lep.mediumMuonId != 1: return False
        #if abs(lep.pdgId) == 11 and (lep.tightId < 1 or (abs(lep.etaSc) > 1.4442 and abs(lep.etaSc) < 1.566)) : return False
        if abs(lep.pdgId) == 11:
          if (abs(lep.etaSc) > 1.4442 and abs(lep.etaSc) < 1.566) : return False
          if (lep.convVeto == 0) or (lep.lostHits > 0) : return False
          if (abs(lep.eta) < 0.8 and lep.mvaIdPhys14 < 0.73) : return False
          if (abs(lep.eta) > 0.8 and abs(lep.eta) < 1.479 and lep.mvaIdPhys14 < 0.57) : return False
          if (abs(lep.eta) > 1.479 and lep.mvaIdPhys14 < 0.05) : return False
          ## loose id if (abs(lep.eta) < 0.8 and lep.mvaIdPhys14 < 0.35) : return False
          ## loose id if (abs(lep.eta) > 0.8 and abs(lep.eta) < 1.479 and lep.mvaIdPhys14 < 0.20) : return False
          ## loose id if (abs(lep.eta) > 1.479 and lep.mvaIdPhys14 < -0.52) : return False
        if lep.miniRelIso > 0.1: return False
        return True

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    tree.vectorTree = True
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf1 = edgeFriends("Edge", 
                lambda lep : _susyEdge(lep),
                cleanJet = lambda lep,jet,dr : (jet.pt < 35 and dr < 0.4 and abs(jet.eta) > 2.4))
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf1(ev)
            print self.sf2(ev)
            print self.sf3(ev)
            print self.sf4(ev)
            print self.sf5(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)
