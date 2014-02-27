from auctiondotcomitems import AuctionDOTcomItems
from lib import groupiter

import re

def AuctionDOTcomGetItems(listing):

    def _popSetItem(_key, _data):
        loop = True
        try:
            while loop:
                _value = str(_data.pop(0))
                _value = _value.lstrip()
                _value = _value.rstrip()
#                 _value = "".join(_value.split())
                if len(_value) > 0:       
                    item[_key] = _value
                    loop = False
        except IndexError, e:
                item[_key] = None
        return item[_key]

    item = AuctionDOTcomItems()

    # Get all the simple xpath info
    item['propertyID'] = ''.join(set(listing.xpath('./@property-id').extract()))
    item['alertBanner'] = ''.join(set(listing.xpath('.//div[@class="primaryAlertBanner listOnly yellow"]').extract())) 
    item['fullAddress'] = ''.join(set(listing.xpath('.//ul[@class="searchResultInfo major"]//li[@class="searchResultAddress"]//a[@class="searchTrackPDP"]//text()').extract()))  #
    item['datailLink'] = ''.join(set(listing.xpath('.//ul[@class="searchResultInfo major"]//li[@class="searchResultAddress"]//a[@class="searchTrackPDP"]//@href').extract()))

    # item['streetNumber'] = ''.join(set(listing.xpath().extract())) # PLACEHOLDER
    # item['street'] = ''.join(set(listing.xpath().extract()))  # PLACEHOLDER
    # item['state'] = ''.join(set(listing.xpath().extract()))  # PLACEHOLDER
    # item['postcode'] = ''.join(set(listing.xpath().extract()))  # PLACEHOLDER
    # item['country'] = ''.join(set(listing.xpath().extract()))  # PLACEHOLDER

    # Get everything from the class="searchResultInfo major"
    # Because the null data (line returns) between the data key and the 
    # data value are not laid out in a consistent manner, we use regex 
    # by popping the data off the stack one at a time, check to see what 
    # data type it matches, and then assume the next NON-NULL value popped 
    # off the stack is the matching value data. 
    
    # Get "the stack" (_data)
    _data = listing.xpath('.//ul[@class="searchResultInfo major"]//li[.//span[contains(@class,"searchResultLabel")]]//text()').extract()
    loop = True
    while loop:
        # Keep popping items off the stack until you hit an index error
        # This returns control outside the loop
        try:
            _item = _data.pop(0) # pop the first item
            _item = "".join(_item.split()) # strip white spaces
            if _item != "": # if not null

                # If it matches the "Asset Type" parameter, send control 
                # to _popSetItem which will continue to pop items off 
                # the stack until it reaches a non-null value. It will 
                # assign this value to item[<first_argument>], or in this 
                # case assign it to item["assetType"]
                if re.match(".*^asset.*type.*$", str(_item).lower()):
                    _popSetItem("assetType", _data)
                    continue
                
                if re.match(".*^foreclosure.*trustee.*$", str(_item).lower()):
                    _popSetItem("ftNum", _data)
                    continue
                
                if re.match(".*^propertyid.*$", str(_item).lower()):
                    _popSetItem("propertyID", _data)
                    continue

                if re.match(".*^item#.*$", str(_item).lower()):
                    _popSetItem("itemNum", _data)
                    continue
                
                if re.match(".*^est.*opening.*bid.*$", str(_item).lower()):
                    _popSetItem("openingBid", _data)
                    continue

                if re.match(".*^auction.*date.*$", str(_item).lower()):
                    _popSetItem("auctionDate", _data)
                    continue

                if re.match(".*^sale.*location.*$", str(_item).lower()):
                    _popSetItem("saleLocation", _data)
                    continue

                if re.match(".*^time.*$", str(_item).lower()):
                    _popSetItem("saleTime", _data)
                    continue
                                                                                                    
        except IndexError, e:
            # Hit the end of stack. Turn off the loop and return control 
            # outside
            loop = False

    # Some of the house data is held in a "HoverOver" script
    # We have to parse this data out using regex, since xpath doesn't like
    # traversing scripts
    
    # .extract() the entire script as a string
    _data = ''.join(set(listing.xpath('.//script[@type="text/html"]').extract()))
    # split it into lines
    for _line in _data.split("\n"):
        # Match only the 2 strings of interest using using re.escape
        _match =  (re.search(
                             re.escape('<li><span class="label">') +
                             "(.*?)" + 
                             re.escape('</span><span class="value">')+
                             "(.*?)" + 
                             re.escape('</span></li>'), 
                    _line))
        # Match by the first string, using second string as the data
        if _match:
            if re.match("^.*county.*$", str(_match.group(1)).lower()): 
                item['county'] = str(_match.group(2))

            if re.match("^.*property.*type.*$", str(_match.group(1)).lower()): 
                item['propertyType'] = str(_match.group(2))

            if re.match("^.*bedroom.*$", str(_match.group(1)).lower()): 
                item['bedrooms'] = str(_match.group(2))
                
            if re.match("^.*bath[s]{0,1}.*$", str(_match.group(1)).lower()): 
                item['bathrooms'] = str(_match.group(2))
                
            if re.match("^.*occupancy.*status.*$", str(_match.group(1)).lower()): 
                item['occupancyStatus'] = str(_match.group(2))
                
            if re.match("^.*lot.*size.*$", str(_match.group(1)).lower()): 
                item['lotSize'] = str(_match.group(2))
                
            if re.match("^.*previous.*value.*$", str(_match.group(1)).lower()): 
                item['previousValue'] = str(_match.group(2))
    
    return item

if __name__ == "__main__":
    from estatescraper import SpiderRun
    from estatescraper import AuctionDOTcom
    spider = AuctionDOTcom()
    r = SpiderRun(spider)