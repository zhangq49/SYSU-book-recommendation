#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class AllBookLabelHandler(BaseHandler):
    def get(self):
        try:
            cookie = super(AllBookLabelHandler, self).get_current_user()
        
            page = self.get_argument('page', '1')

            temp = getAllLabel(int(page), LabelCountPerPage)
            allLabelList = temp[1]
            totalPage = temp[0]

            self.render('allBookLabel.html',
        	   allLabelList=allLabelList,
        	   totalPage=int(totalPage),
        	   curPage=int(page),
        	   )
        except:
            self.write_error(404)
            
    def post(self,):
        pass


    