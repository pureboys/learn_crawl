# -*- coding: utf-8 -*-
import scrapy


class PostDevSpider(scrapy.Spider):
    name = 'post_dev'
    # allowed_domains = ['example.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        for url in self.start_urls:
            # post 请求
            data = {
                'kw': 'cat'
            }
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=data)

    # 基于管道的
    def parse(self, response):
        print(response.text)
