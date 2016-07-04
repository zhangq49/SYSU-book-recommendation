#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from root import *

class BookHandler(BaseHandler):
    def get(self,id):
        try:
            cookie = super(BookHandler, self).get_current_user()
            
            recordVisit(cookie, id)

            temp = getBookInfo(id)
            bookName = temp[0]
            bookPicURL = temp[1]
            author = temp[2]
            press = temp[3]
            score = temp[4]
            scoreNumber = temp[5]
            introduction = temp[6]
            authorIntro = temp[7]
            sysuBookURL = temp[8]
            relatedBookList = temp[9]
            
            popularLabelList = getPopularLabel()
            self.render('book.html',
                temp=temp, bookName=bookName, bookPicURL=bookPicURL,
                author=author, press=press, score=score, scoreNumber=scoreNumber,
                introduction=introduction, authorIntro=authorIntro,
                sysuBookURL=sysuBookURL, relatedBookList=relatedBookList,
                popularLabelList=popularLabelList)
        except:
            self.write_error(404)

    def post(self):
        pass


    