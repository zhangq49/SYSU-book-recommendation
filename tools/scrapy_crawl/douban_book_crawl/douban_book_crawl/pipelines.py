# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..')))
print(sys.path[0])


#from modules.db.models.book import Book
#from modules.db.helper import book as bookHelper
#from modules.db.helper import doulie as doulieHelper

import MySQLdb
import MySQLdb.cursors

reload(sys)
sys.setdefaultencoding('utf8')


class JsonWithEncodingDoubanBookCrawlPipeline(object):
	def __init__(self):
		self.file = codecs.open('douban_book.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		print "------------------------- Processing JsonWithEncodingDoubanBookCrawlPipeline Processing -------------------------"
		line = item["book_info"] + "\n"
		self.file.write(line)
		print "Processing!!!!"
		print "------------------------- Stop JsonWithEncodingDoubanBookCrawlPipeline Stop -------------------------"
		return item
		
	def spider_closed(self, spider):
		self.file.close()

class MySQLStoreDoubanBookCrawPipeline(object):
	def process_item(self, item, spider):
		print "------------------------- Processing MySQLStoreDoubanBookCrawPipeline Processing -------------------------"
		decode_book_info = json.loads(item["book_info"])
		print type(decode_book_info)
		book_name = decode_book_info["title"]
		book_imgUrl = decode_book_info["image"]
		book_isbn = decode_book_info["isbn13"]
		book_author = decode_book_info["author"]
		book_press = decode_book_info["publisher"]
		book_douban_point = decode_book_info["rating"]["average"]
		book_douban_rate_sum = decode_book_info["rating"]["numRaters"]
		book_desc = decode_book_info["summary"]
		book_author_desc = decode_book_info["author_intro"]
		
		print "------------------------- Stop MySQLStoreDoubanBookCrawPipeline Stop -------------------------"
		return item

