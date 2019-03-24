from scrapy.spiders import CSVFeedSpider
from scrapy_practice.items import TestItem

class MySpider(CSVFeedSpider):
    name = 'example.com_CSVFeedSpider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.csv']
    delimiter = ';'
    quotechar = "'"
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)

        item = TestItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item