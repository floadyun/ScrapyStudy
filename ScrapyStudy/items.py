# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


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
