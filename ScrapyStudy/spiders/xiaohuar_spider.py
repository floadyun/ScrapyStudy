import scrapy

class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']
    def parse(self, response):
        current_url = response.url
        body  = response.body
        unicode_body = response.body_as_unicode()