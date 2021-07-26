# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
import logging

class VnexpressPipeline:

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'vnex'
        password = 'root'
        database = 'vnexpress'

        logging.info("connecting to db")
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        logging.info("connected to db")

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
        logging.info("disconnected to db")

    def process_item(self, item, spider):
        # when existing the url in database, ignore and processing next url
        insert = "insert into article_info(url,date,article,title) values(%s,%s,%s,%s) ON CONFLICT (url) DO NOTHING "

        # when having too much request to insert into db in the short time
        try:
            self.cur.execute(insert, (item['url'], item['date'], item['article'], item['title']))
            self.connection.commit()
        except:
            #rollback and try again
            logging.info("rollback data")
            self.cur.execute("rollback")
            logging.info("finish rollback")

            self.cur.execute(insert, (item['url'], item['date'], item['article'], item['title']))
            self.connection.commit()
        return item


