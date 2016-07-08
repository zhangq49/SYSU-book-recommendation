# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..')))
print(sys.path[0])


from modules.db.models.book import Book
from modules.db.helper import book as bookHelper
from modules.db.helper import doulie as doulieHelper

def main():
    print 'isDup'
    print bookHelper.isDup('9787544270878'), 'true'
    print bookHelper.isDup('9787544245555'), 'true'
    print bookHelper.isDup('1823u42342342'), 'false'

    print 'saveBook'
    book = Book('testsavebook1', 'imgurl', 'isbn123423',
        'author', 'press', 10, 100, 'desc', 'authordesc', 'liburl',
        ['label2', 'dygw', 'label4', 'label5'])
    # bookUid = bookHelper.saveBook(book)
    # print 'bookUid', bookUid

    print 'isDoulieDup'
    print doulieHelper.isDoulieDup('1'), 'true'
    print doulieHelper.isDoulieDup(2), 'false'

    print 'saveDoulieUid'
    # doulieHelper.saveDoulieUid('2')
    # doulieHelper.saveDoulieUid(3)

    print 'getBookUid'
    print bookHelper.getBookUid('isbn123423')
    print bookHelper.getBookUid('i23')

main()
