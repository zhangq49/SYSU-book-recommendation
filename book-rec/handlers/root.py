#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from BaseHandler import *

from getPopularBook import *
from getRecommendBook import *
from getPopularLabel import *
from getSearchResult import *
from getAllLabel import *
from getBookInfo import *
from getBookByLabel import *
from recordVisit import *

from modules.db.helper import book
from modules.db.helper import bookLabel

searchBookCountPerPage = 10
LabelCountPerPage = 10
LabelBookCountPerPage = 10
quantityOfPopularBook = 10

