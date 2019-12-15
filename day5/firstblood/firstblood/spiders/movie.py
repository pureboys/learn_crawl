# -*- coding: utf-8 -*-
import scrapy
from firstblood.items import MovieItem
from redis import Redis


class PostDevSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['example.com']
    start_urls = ['https://www.4567tv.tv/frim/index1.html']
    # 非第一页的通用模板
    url = 'https://www.4567tv.tv/frim/index1-%d.html'
    page = 2
    conn = Redis(host='127.0.0.1', port=6379)

    # 基于管道的
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            name = li.xpath('./div/a/@title').extract_first()
            detail_url = 'https://www.4567tv.tv' + li.xpath('./div/a/@href').extract_first()

            item = MovieItem()
            item['name'] = name

            ex = self.conn.sadd('movie_detail_urls', detail_url)
            if ex == 1:
                # 对详情页url发起get请求
                yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'item': item})
            else:
                pass

        if self.page <= 5:
            new_url = format(self.url % self.page)
            self.page += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def detail_parse(self, response):
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc
        yield item
