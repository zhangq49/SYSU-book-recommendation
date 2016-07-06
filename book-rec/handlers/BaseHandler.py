#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tornado.web
import time
import hashlib

from modules.db.helper import user

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        cookie = self.get_secure_cookie("cookie")
        if cookie:
            return cookie
        else:
            cookie = str(time.time())
            user.saveUser(cookie)
            self.set_secure_cookie('cookie', cookie)
            return cookie

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
