# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #排名
    rank = scrapy.Field()
    #名称
    title = scrapy.Field()
    # 影评
    quote = scrapy.Field()
    #海报
    pic = scrapy.Field()
    pass
