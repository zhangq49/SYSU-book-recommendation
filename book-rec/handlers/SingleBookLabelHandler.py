#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class SingleBookLabelHandler(BaseHandler):
    def get(self, name):
        cookie = super(SingleBookLabelHandler, self).get_current_user()

        page = self.get_argument('page', '1')
    
        totalPage = calcPage(book.getBookSumOfLabel(name), sizeOfGetBooksByLabelMethod)

        books = book.getBooksByLabel(name, int(page) - 1, sizeOfGetBooksByLabelMethod)
        labelBookList = formatToBookList(books)

        bookLabels = bookLabel.getLabels(0, sizeOfGetLabelsMethod)
        popularLabelList = formatToPopularLabelList(bookLabels)

        self.render('singleBookLabel.html',
        	labelBookList=labelBookList,
        	popularLabelList=popularLabelList,
        	curPage=int(page),
        	totalPage=int(totalPage),
        	name=name,
        	)


    def post(self,):
        pass


    