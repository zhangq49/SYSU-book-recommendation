#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
根据分类标签name值，调用数据库API，
返回一个该类书籍列表[[id, bookName, bookURL], ]。
'''
def getBookByLabel(name, page, count):
	return [10, [[1, 'C++','www.douban.com/XXXXXXX'], 
	[2, 'python','www.douban.com/XXXXXXX']]]


