import scrapy

class DemoSpider(scrapy.Spider):

    name = 'sample'
    start_urls = ('https://httpbin.org/ip',)

    def parse(self, response):
        print (response.body)