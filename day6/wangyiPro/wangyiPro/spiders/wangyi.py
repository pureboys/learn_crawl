# -*- coding: utf-8 -*-
import scrapy
from wangyiPro.items import WangyiproItem
from selenium import webdriver

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['example.com']
    start_urls = ['https://news.163.com/']

    bro = webdriver.Chrome(executable_path='/home/oliver/Public/learn_crawl/chromedriver')

    urls = []

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        for index in [3, 4, 6, 7, 8]:
            li = li_list[index]
            new_url = li.xpath('./a/@href').extract_first()

            self.urls.append(new_url)

            yield scrapy.Request(url=new_url, callback=self.parse_news)

    # 只能拿到新闻的标题
    def parse_news(self, response):
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            news_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title

            yield scrapy.Request(url=news_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//div[@id="endText"]//text()').extract()
        content = ''.join(content)

        item['content'] = content
        yield item

    def close(self, spider):
        print('爬虫整体结束')
        self.bro.quit()
