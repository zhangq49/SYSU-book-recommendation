#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class SearchHandler(BaseHandler):
    def get(self):
        try:
            cookie = super(SearchHandler, self).get_current_user()

            searchString = self.get_argument('bookName', '')
            searchString = '123'
            page = self.get_argument('page', '1')

            temp = getSearchResult(searchString, int(page), searchBookCountPerPage)
            searchResultBookList = temp[1]
            totalPage = temp[0]
            
            popularLabelList = getPopularLabel()

            self.render('searchResult.html', 
            	searchResultBookList=searchResultBookList,
            	popularLabelList=popularLabelList,
            	totalPage=int(totalPage),
            	curPage=int(page),
            	searchString='searchString'
            	)
        except:
            self.write_error(404)

    def post(self,):
        pass


    