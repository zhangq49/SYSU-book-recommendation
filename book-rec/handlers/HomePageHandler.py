#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class HomePageHandler(BaseHandler):
    def get(self):
        cookie = super(HomePageHandler, self).get_current_user()

        books = book.getPopularBooks(quantityOfPopularBook)
        popularBookList = formatToBookList(books)
        
        books = book.getRecommendedBooks(cookie)
        recommendBookList = formatToBookList(books)

        bookLabels = bookLabel.getLabels(0, sizeOfGetLabelsMethod)
        popularLabelList = formatToPopularLabelList(bookLabels)

        self.render('homePage.html',
        	popularBookList=popularBookList,
        	recommendBookList=recommendBookList,
        	popularLabelList=popularLabelList,
        	
        	)


    def post(self,):
        self.direct('/')


    