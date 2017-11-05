import scrapy
from ScrapyStudy.items import xhItem
class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://tu.duowan.com/m/meinv']
    def parse(self, response):
        item = xhItem()
        xiaohuas = response.xpath('//ul[@id="pic-list"]/li[@class="box"]')
        print(xiaohuas)
        for xiaohua in xiaohuas:
            item['name'] = xiaohua.xpath('.//span[2]/span/text()').extract()
            item['imageUrl'] = xiaohua.xpath('.//a/img/@src').extract()
            yield item
            print(item['name'])
            print(item['imageUrl'])