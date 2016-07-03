#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
根据书籍id值，调用数据库API，
返回书本详细信息列表[书名,书籍图片链接,
作者,出版社,豆瓣分,评分人数,内容简介,
作者简介,中大借阅链接,[[id, bookName, 
bookURL], ] ]

[[id, bookName],]：类似书籍列表

'''
def getBookInfo(id):
	return ['C++', 'http://douban/XXXX', '作者1', 'XX出版社', '豆瓣分10', '20人评分', '内容关于C++', '作者简介XXX', 'http://sysu/library/XXXX',
	[[3, 'Java', 'http://douban/XXXX'], [4, 'HTML', 'http://douban/XXXX']]]
	
	
