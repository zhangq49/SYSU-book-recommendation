#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class SingleBookLabelHandler(BaseHandler):
    def get(self, name):
        try:
            cookie = super(SingleBookLabelHandler, self).get_current_user()

            page = self.get_argument('page', '1')
            temp = getBookByLabel(name, int(page), LabelBookCountPerPage)
            totalPage = temp[0]
            labelBookList = temp[1]
            popularLabelList = getPopularLabel()

            self.render('singleBookLabel.html',
            	labelBookList=labelBookList,
            	popularLabelList=popularLabelList,
            	curPage=int(page),
            	totalPage=int(totalPage),
            	name=name,
            	)
        except:
            self.write_error(404)

    def post(self,):
        pass


    