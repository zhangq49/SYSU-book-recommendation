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
		print "book_name: ", book_name
		book_imgUrl = decode_book_info["image"]
		print "book_imgUrl: ", book_imgUrl
		book_isbn = decode_book_info["isbn13"]
		print "book_isbn: ", book_isbn
		book_author = decode_book_info["author"]
		print "book_author: ", book_author
		book_press = decode_book_info["publisher"]
		print "book_press: ", book_press
		book_douban_point = decode_book_info["rating"]["average"]
		print "book_douban_point: ", book_douban_point
		book_douban_rate_sum = decode_book_info["rating"]["numRaters"]
		print "book_douban_rate_sum: ", book_douban_rate_sum
		book_desc = decode_book_info["summary"]
		print "book_desc: ", book_desc
		book_author_desc = decode_book_info["author_intro"]
		print "book_author_desc: ", book_author_desc
		book_lib_url = item["book_isbn"]
		print "book_lib_url: ", book_lib_url
		book_tags = []
		for tag in decode_book_info["tags"]:
			book_tags.append(tag["name"])
		print "book_tags: ", book_tags
		print "------------------------- Stop MySQLStoreDoubanBookCrawPipeline Stop -------------------------"
		return item

