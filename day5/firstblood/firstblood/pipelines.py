# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from redis import Redis


class FirstbloodPipeline(object):
    fp = None

    def open_spider(self, spider):
        print("开始爬虫...")
        self.fp = open('./quotes.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":" + content + "\n")

        return item  # 返回给了下一个即将被执行的管道类

    def close_spider(self, spider):
        print('结束爬虫...')
        self.fp.close()


class MysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='quotes',
                                    charset='utf8')
        print(self.conn)

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into quote values (null,"%s","%s")' % (item['author'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class RedisPipeline(object):
    conn = None

    def open_spider(self, spider):
        self.conn = Redis(host='127.0.0.1', port=6379)
        print(self.conn)

    def process_item(self, item, spider):
        dic = {
            'author': item['author'],
            'content': item['content']
        }
        self.conn.lpush('quote', dic)  # redis-py使用2.10.6
        return item
