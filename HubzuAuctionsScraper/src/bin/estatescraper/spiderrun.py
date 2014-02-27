from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings

class SpiderRun:
    def __init__(self, spider):
        settings = get_project_settings()
        mySettings = {'ITEM_PIPELINES': {'estatescraper.pipelines.EstatescraperXLSwriter':300}} 
        settings.overrides.update(mySettings)

        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
#         log.start()
        reactor.run() # the script will block here until the spider_closed signal was sent
        self.cleanup()

    def cleanup(self):
        print "SpiderRun done" #333
        pass
        
if __name__ == "__main__":
    from estatescraper import AuctionDOTcom
    spider = AuctionDOTcom()
    r = SpiderRun(spider)