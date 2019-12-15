# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SunlinePipeline(object):
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'SunlineItem':
            print(item['title'], item['net_friend'])
        else:
            print(item['content'])

        return item
