from scrapy.xlib.pydispatch import dispatcher
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy import signals
from scrapy.spider import Spider

from auctiondotcomurls import AuctionDOTcomURLs
from auctiondotcomitems import AuctionDOTcomItems
from auctiondotcomgetitems import AuctionDOTcomGetItems

import urlparse
import time 

import sys

class AuctionDOTcom(Spider):
    def __init__(self,
                 limit = 50, 
                 miles = 250,
                 zip = None, 
                 asset_types = "",
                 auction_types = "", 
                 property_types = ""):
        self.name = "auction.com"
        self.allowed_domains = ["auction.com"]
        self.start_urls = AuctionDOTcomURLs(limit, miles, zip, asset_types, 
                                            auction_types, property_types)

        dispatcher.connect(self.testsignal, signals.item_scraped) 

    def testsignal(self):
        print "in csvwrite" #333
        
    def parse(self, response):
        sel = Selector(response)
        listings =  sel.xpath('//div[@class="contentDetail searchResult"]')
        for listing in listings:
#             item = AuctionDOTcomItems()
# 
#             item['propertyID'] = ''.join(set(listing.xpath('./@property-id').extract()))
#             print "item['propertyID'] = ", item['propertyID'] #333
            item = AuctionDOTcomGetItems(listing)

        ################
        # DEMONSTRATTION ONLY
            print "######################################"            
            for i in item:
                print i + ": " + str(item[i])
        
        next = set(sel.xpath('//a[contains(text(),"Next")]//@href').extract())

        for i in next:
            yield Request("http://%s/%s" % (urlparse.urlparse(response.url).hostname, i), callback=self.parse)


if __name__ == "__main__":
    from estatescraper import SpiderRun
    from estatescraper import AuctionDOTcom
    spider = AuctionDOTcom()
    r = SpiderRun(spider)