# -*- coding: utf-8 -*-
import scrapy
from firstblood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['example.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    # 基于终端指令的
    # def parse(self, response):
    #     div_list = response.xpath('//div[@class="quote"]')
    #     all_data = []
    #     for div in div_list:
    #         auth = div.xpath('.//small/text()').extract_first()
    #         content = div.xpath('./span/text()').extract_first()
    #         dic = {
    #             'author': auth,
    #             'content': content,
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 基于管道的
    def parse(self, response):
        div_list = response.xpath('//div[@class="quote"]')
        for div in div_list:
            auth = div.xpath('.//small/text()').extract_first()
            content = div.xpath('./span/text()').extract_first()

            # 实例化一个item类型的对象
            item = FirstbloodItem()
            # 使用中括号的形式访问item对象中的属性
            item['author'] = auth
            item['content'] = content
            # 将item提交给管道
            yield item

