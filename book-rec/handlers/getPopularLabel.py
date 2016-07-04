#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
调用数据库API进行相关操作，
返回一个热门（点击次数最多）分类标签
列表[[name, content],]。
name：标签链接构成部分。
构成前端中每个标签的链接（/book-Label/name）
content：分类标签中文

'''
def getPopularLabel():
	return ['计算机', '数学']

