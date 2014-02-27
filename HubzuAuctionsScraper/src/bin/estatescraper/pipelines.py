import csv
from csv import DictWriter

# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item

class EstatescraperXLSwriter(object):
    def __init__(self):
        self.Csv = csv.writer(open('test.csv', 'wb'),
        delimiter=',', 
        quoting=csv.QUOTE_MINIMAL)
        self.Csv.writerow(['propertyID',
                            'itemNum',
                            'ftNum',
                            'assetType',
                            'propertyType',
                            'county',
                            'saleTime',
                            'auctionDate',
                            'saleLocation',
                            'openingBid',
                            'previousValue',
                            'bedrooms',
                            'bathrooms',
                            'lotSize',
                            'fullAddress',
                            'occupancyStatus',
                            'datailLink'])

    def open_spider(self, spider):
        pass
    
    def process_item(self, item, spider):
        # Check that all item keys exist in this run
        _list = []
        for _key in ('propertyID',
                    'itemNum',
                    'ftNum',
                    'assetType',
                    'propertyType',
                    'county',
                    'saleTime',
                    'auctionDate',
                    'saleLocation',
                    'openingBid',
                    'previousValue',
                    'bedrooms',
                    'bathrooms',
                    'lotSize',
                    'fullAddress',
                    'occupancyStatus',
                    'datailLink',):
            try:
                _list.append(str(item[_key]))
            except KeyError, e:
                item[_key] = 'Unavailable'
                _list.append(str(item[_key]))
                
        self.Csv.writerow(_list)
#                                         item['propertyID'],
#                                         item['itemNum'],
#                                         item['ftNum'],
#                                         item['assetType'],
#                                         item['propertyType'],
#                                         item['county'],
#                                         item['saleTime'],
#                                         item['auctionDate'],
#                                         item['saleLocation'],
#                                         item['openingBid'],
#                                         item['previousValue'],
#                                         item['bedrooms'],
#                                         item['bathrooms'],
#                                         item['lotSize'],
#                                         item['fullAddress'],
#                                         item['occupancyStatus'],
#                                         item['datailLink'],
#                                         ])
        return item

    def close_spider(self, spider):
        pass


if __name__ == "__main__":
    o = EstatescraperXLSwriter()
    