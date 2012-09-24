import FWCore.ParameterSet.Config as cms

#Full Event content 
RecoJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloJets_*_*_*', 
                                           'keep recoPFJets_*_*_*',
                                           'keep recoTrackJets_*_*_*',
                                           'keep recoJPTJets_*_*_*',
                                           'keep *_caloTowers_*_*', 
                                           'keep *_towerMaker_*_*',
                                           'keep *_CastorTowerReco_*_*',                                           
                                           'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
                                           'keep *_ic5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_iterativeCone5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_iterativeCone5JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_iterativeCone5JetExtender_*_*', 
                                           'keep *_sisCone5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_sisCone5JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_sisCone5JetExtender_*_*', 
                                           'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_kt4JetExtender_*_*',
                                           'keep *_ak5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_ak5JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_ak5JetExtender_*_*',
                                           'keep *_ak5JetTracksAssociatorExplicit_*_*',
                                           'keep *_ak7JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_ak7JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_ak7JetExtender_*_*',
                                           'keep *_ak5JetID_*_*','keep *_ak7JetID_*_*',
                                           'keep *_sc5JetID_*_*','keep *_sc7JetID_*_*',
                                           'keep *_ic5JetID_*_*','keep *_ic7JetID_*_*',
                                           'keep *_gk5JetID_*_*','keep *_gk7JetID_*_*',
                                           'keep *_kt4JetID_*_*','keep *_kt6JetID_*_*',
                                           'keep *_ca4JetID_*_*','keep *_ca6JetID_*_*',
                                           #keep jet area variables for jet colls in RECO 
                                           'keep *_kt4CaloJets_*_*', 
                                           'keep *_kt6CaloJets_*_*',
                                           'keep *_ak5CaloJets_*_*',
                                           'keep *_ak7CaloJets_*_*',
                                           'keep *_iterativeCone5CaloJets_*_*', 
                                           'keep *_iterativeCone15CaloJets_*_*', 
                                           'keep *_kt4PFJets_*_*', 
                                           'keep *_kt6PFJets_*_*',
                                           'keep *_ak5PFJets_*_*',
                                           'keep *_ak7PFJets_*_*',
                                           'keep *_iterativeCone5PFJets_*_*', 
                                           'keep *_JetPlusTrackZSPCorJetAntiKt5_*_*',                              
                                           'keep *_ak5TrackJets_*_*',
                                           'keep *_kt4TrackJets_*_*',
                                           'keep *_ak7BasicJets_*_*',
                                           'keep *_ak7CastorJetID_*_*',
                                           'keep *_fixedGridRho*_*_*'
        )
)
RecoGenJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenJets_*_*_*', 
                                           'keep *_genParticle_*_*')
)
#RECO content
RecoJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_kt4CaloJets_*_*', 
                                           'keep *_kt6CaloJets_*_*',
                                           'keep *_ak5CaloJets_*_*',
                                           'keep *_ak7CaloJets_*_*',
                                           'keep *_iterativeCone5CaloJets_*_*', 
                                           'keep *_iterativeCone15CaloJets_*_*', 
                                           'keep *_kt4PFJets_*_*', 
                                           'keep *_kt6PFJets_*_*',
                                           'keep *_ak5PFJets_*_*',
                                           'keep *_ak7PFJets_*_*',
                                           'keep *_iterativeCone5PFJets_*_*', 
                                           'keep *_JetPlusTrackZSPCorJetAntiKt5_*_*',                                  
                                           'keep *_ak5TrackJets_*_*',
                                           'keep *_kt4TrackJets_*_*',
                                           'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',         
                                           'keep *_caloTowers_*_*', 
                                           'keep *_towerMaker_*_*',
                                           'keep *_CastorTowerReco_*_*',                                           
                                           'keep *_ic5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_iterativeCone5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_iterativeCone5JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_iterativeCone5JetExtender_*_*', 
                                           'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_kt4JetExtender_*_*',
                                           'keep *_ak5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_ak5JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_ak5JetTracksAssociatorExplicit_*_*',
                                           'keep *_ak5JetExtender_*_*',
                                           'keep *_ak7JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_ak7JetTracksAssociatorAtCaloFace_*_*', 
                                           'keep *_ak7JetExtender_*_*',        
                                           'keep *_ak5JetID_*_*','keep *_ak7JetID_*_*',
                                           'keep *_ic5JetID_*_*',
                                           'keep *_kt4JetID_*_*','keep *_kt6JetID_*_*',
                                           'keep *_ak7BasicJets_*_*',
                                           'keep *_ak7CastorJetID_*_*',
                                           'keep double_kt6CaloJetsCentral_*_*',
                                           'keep double_kt6PFJetsCentralChargedPileUp_*_*',
                                           'keep double_kt6PFJetsCentralNeutral_*_*',
                                           'keep double_kt6PFJetsCentralNeutralTight_*_*',
                                           'keep *_fixedGridRho*_*_*'
                                           )
)
RecoGenJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_kt4GenJets_*_*', 
                                           'keep *_kt6GenJets_*_*',
                                           'keep *_ak5GenJets_*_*',
                                           'keep *_ak7GenJets_*_*',
                                           'keep *_iterativeCone5GenJets_*_*', 
                                           'keep *_genParticle_*_*')
    )
#AOD content
RecoJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(#        'keep *_kt4CaloJets_*_*', 
                                           #        'keep *_kt6CaloJets_*_*',
                                           'keep *_ak5CaloJets_*_*',
                                           #        'keep *_ak7CaloJets_*_*',
                                           #        'keep *_iterativeCone5CaloJets_*_*', 
                                           #        'keep *_iterativeCone15CaloJets_*_*', 
                                           #        'keep *_kt4PFJets_*_*', 
                                           #        'keep *_kt6PFJets_*_*',
                                           'keep double_kt6PFJets_rho_*',
                                           'keep *_ak5PFJets_*_*',
                                           'keep *_ak7PFJets_*_*',
                                           #        'keep *_iterativeCone5PFJets_*_*', 
                                           #        'keep *_JetPlusTrackZSPCorJetAntiKt5_*_*',    
                                           'keep *_ak5TrackJets_*_*',
                                           #        'keep *_kt4TrackJets_*_*',
                                           'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',                                             
                                           'keep *_caloTowers_*_*', 
                                           #        'keep *_towerMaker_*_*',
                                           'keep *_CastorTowerReco_*_*',                                           
                                           #        'keep *_ic5JetTracksAssociatorAtVertex_*_*',
                                           'keep *_ak5JetTracksAssociatorAtVertex_*_*', 
                                           'keep *_ak5JetTracksAssociatorExplicit_*_*',
                                           'keep *_ak7JetTracksAssociatorAtVertex_*_*', 
                                           #        'keep *_iterativeCone5JetExtender_*_*', 
                                           'keep *_kt4JetExtender_*_*', 
                                           'keep *_ak5JetExtender_*_*', 
                                           'keep *_ak7JetExtender_*_*',       
                                           'keep *_ak5JetID_*_*',
                                           #        'keep *_ak7JetID_*_*',
                                           #        'keep *_ic5JetID_*_*',
                                           #        'keep *_kt4JetID_*_*','keep *_kt6JetID_*_*',
                                           'keep *_ak7BasicJets_*_*',
                                           'keep *_ak7CastorJetID_*_*',
                                           'keep double_kt6CaloJetsCentral_*_*',
                                           'keep double_kt6PFJetsCentralChargedPileUp_*_*',
                                           'keep double_kt6PFJetsCentralNeutral_*_*',
                                           'keep double_kt6PFJetsCentralNeutralTight_*_*',
                                           'keep *_fixedGridRho*_*_*',
                                           'drop doubles_*Jets_rhos_*',
                                           'drop doubles_*Jets_sigmas_*'
                                           )
    )
RecoGenJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_kt4GenJets_*_*', 
                                           'keep *_kt6GenJets_*_*',
                                           'keep *_ak5GenJets_*_*',
                                           'keep *_ak7GenJets_*_*',
                                           #        'keep *_iterativeCone5GenJets_*_*', 
                                           'keep *_genParticle_*_*'
                                           )
    )
