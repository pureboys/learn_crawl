# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SunlineItem(scrapy.Item):
    title = scrapy.Field()
    net_friend = scrapy.Field()


class SunlineContentItem(scrapy.Item):
    content = scrapy.Field()
