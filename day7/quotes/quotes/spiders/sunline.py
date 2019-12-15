# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quotes.items import SunlineItem, SunlineContentItem


class QuoteSpider(CrawlSpider):
    name = 'sunline'
    # allowed_domains = ['example.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    link = LinkExtractor(allow=r'page=\d+')
    link_detail = LinkExtractor(allow=r'question/2019\d+/\d+\.shtml')

    rules = (
        Rule(link, callback='parse_item', follow=False),
        Rule(link_detail, callback='parse_detail'),
    )

    def parse_item(self, response):
        tr_list = response.xpath('/html/body/div[8]/table[2]//tr')
        for tr in tr_list:
            title = tr.xpath('./td[3]/a[1]/text()').extract_first()
            net_friend = tr.xpath('./td[5]/text()').extract_first()

            item = SunlineItem()
            item['title'] = title
            item['net_friend'] = net_friend
            yield item

    def parse_detail(self, response):
        content = response.xpath('/html/body/div[9]/table[2]//tr[1]/td/div[2]//text()').extract()
        content = ''.join(content)

        item = SunlineContentItem()
        item['content'] = content

        yield item
