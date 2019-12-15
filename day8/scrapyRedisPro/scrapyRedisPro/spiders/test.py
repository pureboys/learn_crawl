# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyRedisPro.items import ScrapyredisproItem
from scrapy_redis.spiders import RedisCrawlSpider


# 进入爬虫文件目录后 执行 scrapy runspider test.py 进入程序挂起状态
# 在redis中执行 lpush ts start_url
# redis 中 items:xxx 为存储的数据


class TestSpider(RedisCrawlSpider):
    name = 'test'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    redis_key = 'ts'  # 可以被共享的调度期中的队列名称
    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('/html/body/div[8]/table[2]//tr')
        for tr in tr_list:
            title = tr.xpath('./td[3]/a[1]/text()').extract_first()
            net_friend = tr.xpath('./td[5]/text()').extract_first()

            item = ScrapyredisproItem()
            item['title'] = title
            item['net_friend'] = net_friend
            yield item
