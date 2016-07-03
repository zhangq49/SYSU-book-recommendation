#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import sys
import re
import urllib

sys.path.append(os.path.join(sys.path[0], 'handlers'))

from HomePageHandler import *
from SearchHandler import *
from AllBookLabelHandler import *
from BookHandler import *
from SingleBookLabelHandler import *
from ErrorHandler import *

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    'debug': 'True',
}

application = tornado.web.Application([
    (r'/', HomePageHandler),
    (r'/search-result', SearchHandler),
    (r'/book-label', AllBookLabelHandler),
    (r'/book/(\d+)', BookHandler),
    (r'/book-label/(.+)', SingleBookLabelHandler),
    (r'/.*', ErrorHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

