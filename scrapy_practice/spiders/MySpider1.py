import scrapy
# MyItem is not defined yet
# from scrapy_practice.items import MyItem

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]

    # def start_requests(self):
    #     yield scrapy.Request('http://www.example.com/1.html', self.parse)
    #     yield scrapy.Request('http://www.example.com/2.html', self.parse)
    #     yield scrapy.Request('http://www.example.com/3.html', self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        # for h3 in response.xpath('//h3').getall():
        #     yield MyItem(title=h3)
        
        # for href in response.xpath('//a/@href').getall():
        #     yield scrapy.Request(response.urljoin(href),self.parse)