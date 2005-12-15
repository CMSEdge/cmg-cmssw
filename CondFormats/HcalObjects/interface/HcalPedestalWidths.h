#ifndef HcalPedestalWidths_h
#define HcalPedestalWidths_h

/** 
\class HcalPedestalWidths
\author Fedor Ratnikov (UMd)
POOL container to store PedestalWidth values 4xCapId
$Author: ratnikov
$Date: 2005/10/06 21:25:32 $
$Revision: 1.5 $
*/

#include <vector>
#include <algorithm>

#include "CondFormats/HcalObjects/interface/HcalPedestalWidth.h"
#include "DataFormats/HcalDetId/interface/HcalDetId.h"

// 
class HcalPedestalWidths {
 public:
  HcalPedestalWidths();
  ~HcalPedestalWidths();
  /// get array of values for 4 capIds
  const HcalPedestalWidth* getValues (HcalDetId fId) const;
  /// get value for given capId = 1..4
  float getValue (HcalDetId fId, int fCapId) const;
  /// get list of all available channels
  std::vector<HcalDetId> getAllChannels () const;
  /// check if data are sorted
  bool sorted () const {return mSorted;}
  /// fill values
  bool addValue (HcalDetId fId, const float fValues [4]);
  /// fill values
  bool addValue (HcalDetId fId, float fValue1, float fValue2, float fValue3, float fValue4);
  /// sort values by channelId  
  void sort ();
  // helper typedefs
  typedef HcalPedestalWidth Item;
  typedef std::vector <Item> Container;
 private:
  Container mItems;
  bool mSorted;
};

#endif
