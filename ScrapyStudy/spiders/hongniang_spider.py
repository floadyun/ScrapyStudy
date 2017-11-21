import scrapy
from ScrapyStudy.items import HongniangItem
from bs4 import BeautifulSoup


class hongniang(scrapy.Spider):
    name = 'hongniang'
    allowed_domains = ['hongniang.com']
    start_urls = ['http://www.hongniang.com/match']

    def parse(self, response):
        # 请求第一页
        yield scrapy.Request(response.url, callback=self.parse_item)
        # 请求其它页
        for page in response.xpath('//div[@class="fy"]/div/a'):
            link = page.xpath('@href').extract()[0]
            yield scrapy.Request('http://www.hongniang.com/match'+link, callback=self.parse_item)

    def parse_item(self, response):
        ul = response.xpath('//ul[@class="waterfall"]')
        for li in ul:
            item = HongniangItem()
            # 注意：xpath获取位置时，不从0开始
            # 用户名
            item["username"] = li.xpath('//div[@class="name"]/a/text()').extract()
            # 相册图片链接
            item["images_url"] = li.xpath('//div[@class="pin_img"]/a/img/@src').extract()
            # 年龄
            item['age'] = li.xpath('//div[@class="xx"]/span[1]/text()').extract()
            # # 地址
            item["place_from"] = li.xpath('//div[@class="xx"]/span[2]/text()').extract()
            # 个人状态
            item['status'] = li.xpath('//div[@class="xx"]/span[3]/text()').extract()
            # # 头像图片链接
            # item["header_link"] = li.xpath('//div[@class=""]')
            # # 内心独白
            item["content"] = li.xpath('//div[@class="db"]/text()').extract()
            # # 学历
            # item["education"] = self.get_education(li)
            # 爱好
        #     item["hobby"] = self.get_hobby(li)
        #     # 个人主页链接
        #     item["source_url"] = response.url
        #     # 数据来源网站
        #     item["source"] = "hongniang"
        #
            yield item

    def get_username(self, response):
        username = response.xpath("//div[@class='name']/text()").extract()
        if len(username):
            username = username[0]
        else:
            username = "NULL"
        return username.strip()

    def get_age(self, response):
        age = response.xpath(
            "//div[@class='mem_main']/div[@class='sub1']/div[@class='right']/div[@class='info2']/div[1]/ul[1]/li[1]/text()").extract()
        if len(age):
            age = age[0]
            print(age)
        else:
            age = "NULL"
        return age.strip()

    def get_header_link(self, response):
        header_link = response.xpath(
            "//div[@class='mem_main']/div[@class='sub1']/div[@class='left']/div[@id='tFocus']/div[@id='tFocusBtn']/div[@id='tFocus-btn']/ul//img[1]/@src").extract()
        if len(header_link):
            header_link = header_link[0]
        else:
            header_link = "NULL"
        return header_link.strip()

    def get_images_url(self, response):
        images_url = response.xpath(
            "//div[@class='pin_img']/a").extract()
        if len(images_url):
            images_url = images_url
        else:
            images_url = "NULL"
        return images_url

    def get_content(self, response):
        ontent = response.xpath(
            "//div[@class='mem_main']/div[@class='sub1']/div[@class='right']/div[@class='info5']/div[@class='text']/text()").extract()
        if len(ontent):
            ontent = ontent[0]
        else:
            ontent = "NULL"
        return ontent.strip()

    def get_place_from(self, response):
        place_from = response.xpath(
            "//div[@class='mem_main']/div[@class='sub2']/div[@class='info1'][1]/div[@class='right']/ul[2]/li[1]/text()").extract()
        if len(place_from):
            place_from = place_from[0]
        else:
            place_from = "NULL"
        return place_from.strip()

    def get_education(self, response):
        education = response.xpath(
            "//div[@class='mem_main']/div[@class='sub1']/div[@class='right']/div[@class='info2']/div/ul[2]/li[2]/text()").extract()
        if len(education):
            education = education[0]
        else:
            education = "NULL"
        return education.strip()

    def get_hobby(self, response):
        hobby = response.xpath(
            "//div[@class='mem_main']//div[@class='sub2']/div[@class='info1'][2]/div[@class='right'][1]/ul[1]/li[4]/text()").extract()
        if len(hobby):
            hobby = hobby[0]
        else:
            hobby = "NULL"
        return hobby.strip()