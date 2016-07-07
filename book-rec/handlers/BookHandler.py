#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from root import *

class BookHandler(BaseHandler):
    def get(self,id):

        cookie = super(BookHandler, self).get_current_user()
        
        recordVisit(cookie, id)

        bookDetail = book.getBookDetail(id)
        bookName = bookDetail.name
        bookPicURL = bookDetail.imgUrl
        author = bookDetail.author
        press = bookDetail.press
        score = bookDetail.doubanPoint
        scoreNumber = bookDetail.doubanRateSum
        introduction = bookDetail.bookDescription
        authorIntro = bookDetail.authorDescription
        sysuBookURL = bookDetail.sysuLibUrl
        isbn = bookDetail.isbn
        books = book.getRelevantBooks(id)
        relatedBookList = formatToBookList(books)
        
        bookLabels = bookLabel.getLabels(0, sizeOfGetLabelsMethod)
        popularLabelList = formatToPopularLabelList(bookLabels)

        bookLabels = book.getBookLabels(id)

        self.render('book.html',
            bookName=bookName, bookPicURL=bookPicURL,
            author=author, press=press, score=score, scoreNumber=scoreNumber,
            introduction=introduction, authorIntro=authorIntro,
            sysuBookURL=sysuBookURL, relatedBookList=relatedBookList,
                popularLabelList=popularLabelList, isbn=isbn, bookLabels=bookLabels)


    def post(self):
        pass


    