# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ScrapystudyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class xhItem(scrapy.Item):
    name = scrapy.Field()
    imageUrl = scrapy.Field()
    title = scrapy.Field()

class bookItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    ratings = scrapy.Field()
    description = scrapy.Field()

class HongniangItem(scrapy.Item):
    # define the fields for your item here like:
    # 用户名
    username = Field()
    # 年龄
    age = Field()
    # 头像图片链接
    header_link = Field()
    # 相册图片链接
    images_url = Field()
    # 状态
    status = Field()
    # 内心独白
    content = Field()
    # 籍贯
    place_from = Field()
    # 学历
    education = Field()
    # 爱好
    hobby = Field()
    # 个人主页链接
    source_url = Field()
    # 数据来源网站
    source = Field()