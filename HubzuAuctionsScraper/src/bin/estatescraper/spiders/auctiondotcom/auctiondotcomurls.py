
from auctiondotcomparams import auctiondotcomparams

import re

def AuctionDOTcomURLs(limit = 50, 
                      miles = 250,
                      zip = None, 
                      asset_types = "",
                      auction_types = "", 
                      property_types = ""):
    """
    auctiondotcomurls([limit, miles, zip, 
                       asset_types, auction_types, property_types])
    
        Returns the URL string to be used at auction.com to return pages of 
        listings, which are subsequently searched for data. 
    
        SUPPORTING FILES: 
            auctiondotcompamas.py
                Is called as a method, not imported. 
                I.e. 
                    (asset_type_dict, 
                     auction_type_dict, 
                     property_type_residential_dict, 
                     property_type_commercial_dict, 
                     property_type_notes_dict) = auctiondotcomparams()
        
    PARAMETERS (All are optional):
        limit = Number of listings per search. 
                50 is the max.
                Defaults to 50.
                
        miles = How many miles away from search zip code to include. 
                250 is the max. 
                Defaults to 250
                Ignored if no zip code included.
        
        zip   = Zip code epicenter form which to search. 
                Defaults to None.
        
        asset_types = A string including the asset types to include in the 
                      search.
                      Recognized options are ...
                          Bank_Owned_Occupied, 
                          Bank_Owned_Vacant
                          Newly_Foreclosed
                          Redemption
                      NOTE: asset_types only apply to bank owned RESIDENTIAL 
                            properties. As such, including asset_types will
                            nullify other non-residential search parameters. 
                            This is a limitation of the site not the method. 
                          
        auction_types = The different categories as defined by the site.
                        These are used in conjunction with the property_types
                        parameter to get the specific listings. 
                        Recognized options are ...
                            residential
                            commercial
                            land (land only)
                            notes
                            
        property_types = Sets the specific property types to be included. 
                         Property types that are counterindictaed by other 
                         parameters (such as asset_types or auction_types)
                         are ignored. 
                         Recognized options are ...
                            condo
                            townhouse
                            Condo_Townhouse
                            Single-family
                            Multi-family
                            Land+Only
                            Retail
                            Office
                            Industrial
                            Hotel
                            Mobile_Home_Park
                            Self-Storage
                            Mixed-Use
                            Special+Purpose
    """
    auction_types = str(auction_types)
    property_types = str(property_types)
    URL = "http://www.auction.com/search?"
    (asset_type_dict, 
     auction_type_dict, 
     property_type_residential_dict, 
     property_type_commercial_dict, 
     property_type_notes_dict) = auctiondotcomparams()
        
    def _check_integer(number, varname):
        """
        _check_integer(number, varname)
        
        Hidden method (do not override)
        
        Checks number is an integer. Raises exception if not. 
        """
        number = "".join(c for c in str(number) if c in "0123456789")
        try:
            # Convert to integer (works even if already an integer)
            # This will raise an exception if there were no numbers in "miles"
            number = int(number)
            return number
        except ValueError, e:
            e = ("auctiondotcomurls(): Parameter '" + 
                 str(varname) + 
                 "' does not appear to be a valid number. " 
                 + str(e))
            raise  ValueError(e)        
    
    def _addlimit(URL, limit):
        """
        _addlimit(URL, limit)
        
        Hidden method (do not override)
        
        Adds the page limit to the HTTP string.  
        """
        limit = _check_integer(limit, "limit")
        URL = URL + "&limit=" + str(limit)
        return URL
    
    def _addmiles(URL, miles):
        """
        _addmiles(URL, miles)
        
        Hidden method (do not override)
        
        Adds the miles to the HTTP search string.  
        """        
        # If no "miles" parameter called, miles = 250 so will always be a num
        miles = _check_integer(miles, "miles")
        # Miles is now an integer
        # Check for allowed miles setting (otherwise site defaults to 5)
        # Maximum miles is 250
        if miles > 250: miles = 250
        # Set miles to one of the allowed ranges
        # Allowed numbers must be a list
        # Change 'allowed' only if allowed search distances on site change
        allowed = [5, 10, 25, 50, 100, 250]
        check1 = 0
        try:
            loop = True
            while loop:
                check2 = allowed.pop(0)
                if ((miles >= check1) and (miles <= check2)):
                    miles = check2
                    loop = False
                else:
                    check1 = check2
        except IndexError:
            loop = False
        URL = URL + "&miles=" + str(miles)
        return URL

    def _addzip(URL, zip):
        """
        _addzip(URL, zip)
        
        Hidden method (do not override)
        
        Adds the zip code epicenter to the HTTP search string.  
        """        
        if zip is not None:
            zip = _check_integer(zip, "zip")
            if len(str(zip)) == 5:
                URL = URL + "&search=" + str(zip)
            else:
                e = ("auctiondotcomurls(): Parameter 'zip' does not " +
                     "appear to be a valid US zip code. ")
                raise  ValueError(e)
        return URL

#-------------------------------------

    def _add_asset_type(URL, http_option):
        """
        _add_asset_type(URL, http_option)
        
        Hidden method (do not override)
        
        Adds the actual asset types to the HTTP search string.
        Called only by _parse_asset_type()  
        """
        # The asset_type string is only ever added by this function so
        #  we check it exactly (no need for regex)
        # If a type has already been added, we use the "%2C" conjunction
        # in the URL otherwise we use "&"
        def _add_it(URL, http_option):
            if "asset_type=" in URL:
                URL = URL + "%2C" + http_option            
            else:
                URL = URL + "&asset_type=" + http_option
            return URL
        URL = _add_it(URL, http_option)
        return URL    

    def _parse_asset_types(URL, asset_types, asset_type_dict):
        """
        _parse_asset_types(URL, asset_types, asset_type_dict)
        
        Hidden method (do not override)
        
        Calculates the asset types to be added to the HTTP search string.
        Calls _add_asset_type(URL, http_option)  
        """        
        for p in asset_type_dict.keys():
            http_option = asset_type_dict[p]
            if (
                re.match(str(p).lower(), str(asset_types).lower())
                or "all" in str(asset_types).lower()
                ):
                URL = _add_asset_type(URL, http_option) 
        return URL
        
    def _parse_property_types(URL, property_types):
        """
        _parse_property_types(URL, property_types)
        
        Hidden method (do not override)
        
        Calculates the property types to be added to the HTTP search string.
        """        
        # all properties will be added to URL using the "properties_type" str
        # We don't add the string thats in the 'property_types' option
        # Instead we add the controlled string we know that the site wants
        # It must always be a string
        # format "regex_match_string":"key_added_toURL"
        # The properties_type string is only ever added by this function so
        #  we check it exactly (no need for regex)
        # If a type has already been added, we use the "%2C" conjunction
        # in the URL otherwise we use "&"

        def _add_it(URL, http_option):
            if "property_type=" in URL:
                URL = URL + "%2C" + http_option            
            else:
                URL = URL + "&property_type=" + http_option
            return URL

        def _parse_it(URL, _dict, _type):
            for p in _dict.keys():
                http_option = _dict[p]
                if re.match(str(p).lower(), str(property_types).lower()):
                    if _type is not None:
                        new_http_option = str(http_option) + "+" + str(_type)
                    else:
                         new_http_option = str(http_option)
                    URL = _add_it(URL, new_http_option)
            return URL     
                
        _types = "".join(auction_types.split())
        _types = str(_types).lower()

        # DO NOT use elif in these
        if "residential" in _types:
            URL = _parse_it(URL, property_type_residential_dict, None)

        if "commercial" in _types: 
            URL = _parse_it(URL, property_type_commercial_dict, "Commercial")

        if "note" in _types:
            URL = _parse_it(URL, property_type_notes_dict, "Notes")

        if "land" in _types:
            if "property_type=" in URL:
                URL = (URL + "%2CLand+Only")
            else:
                URL = (URL + "&property_type=Land+Only")
            URL = URL + "%2CLand+Only+Commercial" + "%2CLand+Only+Notes" 
        return URL
                    
    # Main
    # Must be called in order
    URL = _addzip(URL, zip)
    URL = _addmiles(URL, miles)
    URL = _addlimit(URL, limit)
    URL = _parse_asset_types(URL, asset_types, asset_type_dict)
    URL = _parse_property_types(URL, property_types)
    return [URL]

if __name__ == "__main__":
    o = auctiondotcomurls(
                          miles="24", 
#                           asset_types = "all",
                        auction_types = "commercial residential notes land",
                        property_types = "condo townhouse single family Multi Family Retail Office Industrial Hotel Mobile Home+Park Self Storage Mixed Use  Residential Special Purpose",
                        )
    