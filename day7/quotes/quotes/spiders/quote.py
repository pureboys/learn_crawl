# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QuoteSpider(CrawlSpider):
    name = 'quote'
    # allowed_domains = ['example.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    link = LinkExtractor(allow=r'http://quotes.toscrape.com/page/\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
