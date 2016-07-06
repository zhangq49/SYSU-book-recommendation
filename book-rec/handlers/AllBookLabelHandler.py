#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class AllBookLabelHandler(BaseHandler):
    def get(self):

        cookie = super(AllBookLabelHandler, self).get_current_user()
    
        page = self.get_argument('page', '1')

        labels = bookLabel.getLabels(int(page) - 1, LabelCountPerPage)
        allLabelList = formatToAllLabelList(labels)
        
        totalPage = calcPage(bookLabel.getLabelSum(), LabelCountPerPage)

        self.render('allBookLabel.html',
    	   allLabelList=allLabelList,
    	   totalPage=int(totalPage),
    	   curPage=int(page),
    	   )

            
    def post(self,):
        pass


    