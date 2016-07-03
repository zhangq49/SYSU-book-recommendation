#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
函数通过调用数据库API并进行相关操作，
找出n个热门书籍（点击次数最多），
返回一个热门书籍
列表[[id, bookName, bookURL], ]。

id：书籍编号，构成前端中每个书籍的链接（/book/id）
bookName：书籍的名称
bookURL：豆瓣书籍图片链接
'''
def getPopularBook():
	return [[1, 'C++','www.douban.com/XXXXXXX'], 
	[2, 'python','www.douban.com/XXXXXXX']]

