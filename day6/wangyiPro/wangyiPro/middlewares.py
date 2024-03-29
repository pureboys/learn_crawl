# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep


class WangyiproDownloaderMiddleware(object):

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        if request.url in spider.urls:

            bro = spider.bro
            bro.get(request.url)

            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)

            page_text = bro.page_source
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
