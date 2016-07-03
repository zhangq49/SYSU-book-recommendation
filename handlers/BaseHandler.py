#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tornado.web
import time
import hashlib

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        cookie = self.get_secure_cookie("cookie")
        if cookie:
            return cookie
        else:
            cookie = time.time()
            self.set_secure_cookie('cookie', str(time.time()))
            return cookie

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
