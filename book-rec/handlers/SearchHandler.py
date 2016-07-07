#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class SearchHandler(BaseHandler):
    def get(self):
        try:
            cookie = super(SearchHandler, self).get_current_user()

            searchString = self.get_argument('bookName', '')

            page = self.get_argument('page', '1')

            books = book.searchBooks(searchString, int(page) - 1, searchBookCountPerPage)
            searchResultBookList = formatToBookList(books)

            totalPage = calcPage(len(book.searchBooks(searchString, 0, allResultCount)), searchBookCountPerPage)
            
            bookLabels = bookLabel.getLabels(0, sizeOfGetLabelsMethod)
            popularLabelList = formatToPopularLabelList(bookLabels)

            self.render('searchResult.html', 
            	searchResultBookList=searchResultBookList,
            	popularLabelList=popularLabelList,
            	totalPage=int(totalPage),
            	curPage=int(page),
            	searchString=searchString,
            	)
        except:
            self.write_error(404)

    def post(self,):
        self.write_error(404)


    