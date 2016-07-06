#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class HomePageHandler(BaseHandler):
    def get(self):
        try:
            cookie = super(HomePageHandler, self).get_current_user()
            
            # popularBookList = book.getPopularBooks(quantityOfPopularBook)
            # recommendBookList = book.getRecommendedBooks(cookie)
            popularBookList = getPopularBook()
            recommendBookList = getRecommendBook(cookie)
            popularLabelList = getPopularLabel()

            self.render('homePage.html',
            	popularBookList=popularBookList,
            	recommendBookList=recommendBookList,
            	popularLabelList=popularLabelList,
            	
            	)
        except:
            self.write_error(404)

    def post(self,):
        self.direct('/')


    