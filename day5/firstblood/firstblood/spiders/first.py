# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['example.com']
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left/div"]')
        for div in div_list:
            # auth = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            auth = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)
            print(auth, content)
