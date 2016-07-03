#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
根据用户cookie值，调用数据库API进行相关操作，
根据用户浏览记录利用推荐算法，找出推荐书籍，
并返回一个推荐书籍
列表[[id，bookName, bookURL],]。
'''
def getRecommendBook(cookie):
	return [[1, 'C++','www.douban.com/XXXXXXX'], 
	[2, 'python','www.douban.com/XXXXXXX']]

