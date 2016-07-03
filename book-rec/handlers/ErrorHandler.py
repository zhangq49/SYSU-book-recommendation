#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from root import *

class ErrorHandler(BaseHandler):
    def get(self):
        self.write_error(404)
            
    def post(self,):
        self.write_error(404)


    