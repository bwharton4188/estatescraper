import csv
from csv import DictWriter

# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item

class EstatescraperXLSwriter(object):
    def __init__(self):
        print "Ive started the __init__ in the pipeline" #333

        self.brandCategoryCsv = csv.writer(open('test.csv', 'wb'),
        delimiter=',', 
        quoting=csv.QUOTE_MINIMAL)
        self.brandCategoryCsv.writerow(['Property ID', 'Asset Type'])

    def open_spider(self, spider):
        print "Hit open_spider in EstatescraperXLSwriter" #333
    
    def process_item(self, item, spider):
        print "attempting to run process_item" #333
        self.brandCategoryCsv.writerow([item['propertyID'],
                                        item['assetType']])
        return item

    def close_spider(self, spider):
        print "Hit close_spider in EstatescraperXLSwriter" #333
        pass


if __name__ == "__main__":
    
    o = EstatescraperXLSwriter()
    