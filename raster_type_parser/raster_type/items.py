# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RasterTypeItem(scrapy.Item):
    long_name = scrapy.Field()
    short_name = scrapy.Field()
    flag = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
