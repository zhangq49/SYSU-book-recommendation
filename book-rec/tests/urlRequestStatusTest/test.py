#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import URLRequest
import unittest
import random

class TestCase(unittest.TestCase):
	def setUp(self):
		self.root = 'http://meetbook.applinzi.com/'
		self.urlRequest = URLRequest.URLRequest()
		self.urlRequest.getCookie()
		self.stringList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.?~!@#$^&*()'
	def tearDown(self):
		pass

	def getRandomNumber(self, a=0, b=100):
		return random.randint(a, b)

	def getRandomStringSet(self, number = 10):
		stringset = []
		for j in range(0, number + 1):
			length = self.getRandomNumber(5, 30)
			string = ''
			for i in range(0, length):
				string += random.choice(self.stringList)
			stringset.append(string)
		return stringset

	def testHomePageUrl(self):
		status = self.urlRequest.getHomePageStatus()
		self.assertEqual(status, 200, 'HomePage correct test fail.' + str(status) + '!= 200\n') 

		status = self.urlRequest.getHomePageStatus(self.root + 'abcde')
		self.assertEqual(status, 200, 'HomePage error test fail.' + str(status) + '!= 200\n')

		#随机测试
		stringset = self.getRandomStringSet(10)
		for string in stringset:
			status = self.urlRequest.getHomePageStatus(self.root + string)
			self.assertEqual(status, 200, 'HomePage error test fail.' + str(status) + '!= 200\n')			

	def testSearchResultUrl(self):
		status = self.urlRequest.getSearchResultStatus()
		self.assertEqual(status, 200, 'SearchResult Page correct test fail.' + str(status) + '!= 200\n')

		status = self.urlRequest.getSearchResultStatus('C++', 100)
		self.assertEqual(status, 200, 'SearchResult Page correct test fail.' + str(status) + '!= 200\n')

		status = self.urlRequest.getSearchResultStatus('杂货店', 100)
		self.assertEqual(status, 200, 'SearchResult Page correct test fail.' + str(status) + '!= 200\n')

		status = self.urlRequest.getSearchResultStatus('', -1)
		self.assertEqual(status, 200, 'SearchResult Page error test fail.' + str(status) + '!= 200\n')

		#随机测试
		stringset = self.getRandomStringSet(10)
		for bookName in stringset:
			page = self.getRandomNumber(-100, 100)
			status = self.urlRequest.getSearchResultStatus(bookName, page)
			self.assertEqual(status, 200, 'SearchResult Page error test fail.' + str(status) + '!= 200\n')

	def testAllBookLabelUrl(self):
		status = self.urlRequest.getAllBookLabelStatus()
		self.assertEqual(status, 200, 'AllBookLabel Page correct test fail.' + str(status) + '!= 200\n')

		testList = [0, 10000, -0, -100, -1]
		for page in testList:
			status = self.urlRequest.getAllBookLabelStatus(page)
			self.assertEqual(status, 200, 'AllBookLabel Page error test fail.' + str(status) + '!= 200\n')

	def testBookUrl(self):
		status = self.urlRequest.getBookStatus()
		self.assertEqual(status, 200, 'Book Page correct test fail.' + str(status) + '!= 200\n')

		testList = [0, 10000, -0, -100, -1]
		for bookId in testList:
			status = self.urlRequest.getBookStatus(bookId)
			self.assertEqual(status, 200, 'Book Page error test fail.' + str(status) + '!= 200\n')


	def testSingleBookLabel(self):
		status = self.urlRequest.getSingleBookLabelStatus()
		self.assertEqual(status, 200, 'SingleBookLabel Page correct test fail.' + str(status) + '!= 200\n')

		status = self.urlRequest.getSingleBookLabelStatus('computer', 0)
		self.assertEqual(status, 200, 'SingleBookLabel Page correct test fail.' + str(status) + '!= 200\n')
		#随机测试
		stringset = self.getRandomStringSet(10)
		for name in stringset:
			page = self.getRandomNumber(-100, 100)
			status = self.urlRequest.getSingleBookLabelStatus(name, page)
			self.assertEqual(status, 200, 'SingleBookLabel Page error test fail.' + str(status) + '!= 200\n')



if __name__ == '__main__':
	unittest.main()
	# homePageUrl = "http://meetbook.applinzi.com/" 
	# searchResultUrl = homePageUrl + 'search-result?'
	# url = searchResultUrl + 'searchString=' + u'阿斯顿'+ '&page='
	# print url