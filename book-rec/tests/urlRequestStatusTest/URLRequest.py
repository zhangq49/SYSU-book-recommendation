#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# test the the status of requesting the url

import urllib
import urllib2
import cookielib

class URLRequest(object):
	def __init__(self):
		self.homePageUrl = "http://meetbook.applinzi.com/" 
		self.searchResultUrl = self.homePageUrl + 'search-result?'
		self.allBookLabelUrl = self.homePageUrl + 'book-label?'
		self.bookUrl = self.homePageUrl + 'book/'
		self.singleBookLabelUrl = self.homePageUrl + 'book-label/'
		self.cookieDic = None
		self.cookie = None

	def getCookieDic(self):
		cookieSet = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieSet))
		resp = opener.open(self.homePageUrl)
		cookieDic = dict()
		for cookie in cookieSet:
			cookieDic[cookie.name] = cookie.value
		self.cookieDic = cookieDic

	def getCookie(self):
		self.getCookieDic()
		self.cookie = self.cookieDic['cookie']

	def getStatus(self, url):
		cookie = self.getCookie()
		opener = urllib2.build_opener()
		opener.addheaders.append(('cookie', self.cookie))
		resp = opener.open(url)
		return resp.getcode()

	def getHomePageStatus(self, url=''):
		if not url:
			url = self.homePageUrl
		return self.getStatus(url)

	def getSearchResultStatus(self, searchString='解忧', page=0):
		url = self.searchResultUrl + 'searchString=' + searchString + '&page=' + str(page)
		return self.getStatus(url)

	def getAllBookLabelStatus(self, page=0):
		url = self.allBookLabelUrl + 'page=' + str(page)
		return self.getStatus(url)

	def getBookStatus(self, bookId=1):
		url = self.bookUrl + str(bookId)
		return self.getStatus(url)

	def getSingleBookLabelStatus(self, name='dygw', page=1):
		url = self.singleBookLabelUrl + name + '?page=' + str(page)
		return self.getStatus(url)



