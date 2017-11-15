import scrapy
from ScrapyStudy.items import bookItem
#抓取豆瓣书本数据
class douban_spider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        print(response.url)
        # 请求第一页
        yield scrapy.Request(response.url, callback=self.parse_next)
        # 请求其它页
        for page in response.xpath('//div[@class="paginator"]/a'):
            link = page.xpath('@href').extract()[0]
            yield scrapy.Request(link, callback=self.parse_next)

    def parse_next(self, response):
        for item in response.xpath('//tr[@class="item"]'):
            book = bookItem()
            book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
            book['author'] = item.xpath('td[2]/div[1]/span/text()').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
            book['description'] = item.xpath('td[2]/p/text()').extract()[0]
            yield book
