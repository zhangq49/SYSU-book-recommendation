#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
根据用户提交的表单内容，
调用数据库API进行书籍的模糊查询。
返回一个书籍
列表[[id, bookName, bookURL, ]。
page表示当前页数，count表示元素数量/每页
'''
def getSearchResult(searchString, page, count):
	return [10, [[1, 'C++','www.douban.com/XXXXXXX'], 
	[2, 'python','www.douban.com/XXXXXXX']]]

