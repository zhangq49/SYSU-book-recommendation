# -*- coding: utf-8 -*-

from modules.db.models.book import Book
from modules.db.helper import mysqlConn

@mysqlConn
def isDup(isbn, cur, conn):
    sql = '''select id from book where isbn = %s'''
    cur.execute(sql, isbn)
    rec = cur.fetchone()
    return bool(rec)

@mysqlConn
def saveBook(book, cur, conn):
    '''
    Note: This function will return the id of the book.
    '''
    if not book.isbn:
        # Error
        return
    sql = '''insert into book(name, imgUrl, isbn, author, press, doubanPoint,
        doubanRateSum, bookDescription, authorDescription, sysuLibUrl)
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cur.execute(sql, (book.name, book.imgUrl, book.isbn, book.author,
        book.press, book.doubanPoint, book.doubanRateSum, book.bookDescription,
        book.authorDescription, book.sysuLibUrl))
    #
    sql = '''select uid from book where isbn = %s order by id desc limit 1'''
    cur.execute(sql, book.isbn)
    bookUid = cur.fetchone()[0]
    #
    saveLabels(bookUid, book.labels, cur, conn)
    return bookUid


def saveLabels(bookUid, labels, cur, conn):
    labels = list(set(labels))
    labels = '(%s)' % ','.join(labels)
    sql = '''select name from bookLabel where name in ''' + labels
    num = cur.execute(sql)
    dupLabels = cur.fetchmany(num)
    dupLabels = [item[0] for item in dupLabels]
    newLabels = [(label,) for label in labels if label not in dupLabels]
    # increase counters of duplicate labels
    dupLabelsRange = '(%s)' % ','.join(dupLabels)
    sql = '''update bookLabel set useCount = useCount + 1 where name in ''' \
          + dupLabelsRange
    cur.execute(sql)
    # insert new lables into tables
    sql = '''insert into bookLabel(name, useCount) values(%s, 1)'''
    cur.executemany(sql, newLabels)
    # get all labels' uid, and bound them with bookUid
    sql = '''select uid from bookLabel where name in ''' + labels
    num = cur.execute(sql)
    records = cur.fetchmany(num)
    allLabels = [item[0] for item in records]
    sql = '''insert into labelOfBook(bookUid, bookLabelUid) values
          ({}, %s)'''.format(bookUid)
    cur.executemany(sql, allLabels)
    conn.commit()

    
