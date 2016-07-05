# -*- coding: utf-8 -*-

'''
This file shows some examples of dbhelpers.
'''

from modules.db.helper import book as bookHelper

def printBookSimple(books):
    for book in books:
        print book.uid, book.name, book.imgUrl

def printBookDetail(book):
    print '\n'.join([
        str(book.uid), book.name, book.imgUrl, book.isbn, book.author, book.press,
        str(book.doubanPoint), str(book.doubanRateSum), book.bookDescription,
        book.authorDescription, book.sysuLibUrl])

def main():
    print '-'*40
    print 'getPopularBooks'
    books = bookHelper.getPopularBooks(3)
    printBookSimple(books)

    print '-'*40
    print 'getRecommendedBooks'
    books = bookHelper.getRecommendedBooks('olduser')
    printBookSimple(books)
    print '-'
    books = bookHelper.getRecommendedBooks('newuser')
    printBookSimple(books)

    print '-'*40
    print 'searchBooks'
    print u'嫌疑人'
    books = bookHelper.searchBooks(u'嫌疑人', 0, 5)
    printBookSimple(books)
    print u'东野圭吾'
    books = bookHelper.searchBooks(u'东野圭吾', 0, 2)
    printBookSimple(books)
    print '-'
    books = bookHelper.searchBooks(u'东野圭吾', 1, 2)
    printBookSimple(books)
    print '-'
    books = bookHelper.searchBooks(u'东野圭吾', 2, 2)
    printBookSimple(books)

    print '-'*40
    print 'getBookDetail'
    book = bookHelper.getBookDetail(1)
    printBookDetail(book)

    print '-'*40
    print 'getRelevantBooks'
    books = bookHelper.getRelevantBooks(1)
    printBookSimple(books)

    print '-'*40
    print 'getBooksByLabel'
    books = bookHelper.getBooksByLabel('dygw', 0, 2)
    printBookSimple(books)
    print '-'
    books = bookHelper.getBooksByLabel('dygw', 1, 2)
    printBookSimple(books)
    print '-'
    books = bookHelper.getBooksByLabel('label2', 0, 2)
    printBookSimple(books)
    print '-'
    books = bookHelper.getBooksByLabel('nolabel', 0, 2)
    printBookSimple(books)

    print 'incBookViewCount'
    bookHelper.incBookViewCount('olduser', 1)
    bookHelper.incBookViewCount('newuser', 1)
    bookHelper.incBookViewCount('olduser', 1)
    bookHelper.incBookViewCount('newuser', 2)
    bookHelper.incBookViewCount('no-user', 1)

main()