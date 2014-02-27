def auctiondotcomparams():
    # Asset type is only for bank owned properties
    asset_type_dict = {
        "^.*bank.?owned.?occupied.*$":"Bank_Owned_Occupied",
        "^.*bank.?owned.?vacant.*$":"Bank_Owned_Vacant",
        "^.*newly.?foreclosed.*$":"Newly_Foreclosed",
        "^.*redemption.*$":"Redemption",
    }
        
    auction_type_dict = {
    "default"              :"allAssetType",
    "^.*residential.*$"    :"residential", 
    "^.*commercial.*$"     :"commercial", 
    "^.*land.*$"           :"land", 
    "^.*notes.*$"          :"notes"
    }
        
    property_type_residential_dict = {
        "^.*condo.*$"           :"Condo+Townhouse",
        "^.*townhouse.*$"       :"Condo+Townhouse",
        "^.*single.?family.*$"  :"Single-family",
        "^.*multi.?family.*$"   :"Multi-family", 
        "^.*land.*$"            :"Land+Only",
        }
    
    property_type_commercial_dict = {
        "^.*multi.?family.*$"   :"Multi-family", 
        "^.*retail.*$"          :"Retail",
        "^.*office.*$"          :"Office",
        "^.*industrial.*$"      :"Industrial",
        "^.*hotel.*$"           :"Hotel",
        "^.*mobile.?home.?park.*$":"Mobile+Home+Park",
        "^.*self.?storage.*$"   :"Self-Storage",
        "^.*mixed.*$"           :"Mixed-Use",
        "^.*residential.*$"     :"Residential",
        "^.*special.?purpose.*$":"Special+Purpose",
        "^.*land.*$"            :"Land+Only",
        }
    
    property_type_notes_dict = {
        "^.*multi.?family.*$"   :"Multi-family", 
        "^.*retail.*$"          :"Retail",
        "^.*office.*$"          :"Office",
        "^.*industrial.*$"      :"Industrial",
        "^.*hotel.*$"           :"Hotel",
        "^.*mobile.?home.?park.*$":"Mobile+Home+Park",
        "^.*self.?storage.*$"   :"Self-Storage",
        "^.*mixed.*$"           :"Mixed-Use",
        "^.*residential.*$"     :"Residential",
        "^.*special.?purpose.*$":"Special+Purpose",
        "^.*land.*$"            :"Land+Only",    
    }
    
   
    return asset_type_dict, auction_type_dict, property_type_residential_dict, property_type_commercial_dict, property_type_notes_dict