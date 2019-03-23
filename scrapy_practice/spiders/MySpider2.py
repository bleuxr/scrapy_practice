import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider2'

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.example.com/categories/%s' % category]
        # ...

# import scrapy

# class MySpider(scrapy.Spider):
#     name = 'myspider2'

#     def start_requests(self):
#         yield scrapy.Request('http://www.example.com/categories/%s' % self.category)