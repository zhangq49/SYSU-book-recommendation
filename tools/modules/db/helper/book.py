# -*- coding: utf-8 -*-

from modules.db.models.book import Book
from modules.db.helper import mysqlConn

@mysqlConn
def isDup(isbn, cur, conn):
    sql = '''select uid from book where isbn = %s'''
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
    sql = '''select uid from book where isbn = %s order by uid desc limit 1'''
    cur.execute(sql, book.isbn)
    bookUid = cur.fetchone()[0]
    #
    if book.labels:
        saveLabels(bookUid, book.labels, cur, conn)
    conn.commit()
    return bookUid

def makeSQLRange(seq):
    '''
    Format sequence is python to sql.
    t = ('a', 'b')
    makeRange(t) returns "('a', 'b')"
    '''
    if not seq:
        print 'Error: Empty Set!'
    lst = ["'%s'" % item for item in seq]
    string = '(%s)' % (','.join(lst))
    return string

def saveLabels(bookUid, labels, cur, conn):
    labels = list(set(labels))
    # Get existing labels in :Param lables:
    labelRange = makeSQLRange(labels)
    sql = '''select name from bookLabel where name in ''' + labelRange
    num = cur.execute(sql)
    records = cur.fetchmany(num)
    dupLabels = [item[0] for item in records]
    newLabels = [(label,) for label in labels if label not in dupLabels]
    # increase counters of duplicate labels
    dupLabelRange = makeSQLRange(dupLabels)
    sql = '''update bookLabel set useCount = useCount + 1 where name in ''' \
          + dupLabelRange
    cur.execute(sql)
    # insert new lables into tables
    sql = '''insert into bookLabel(name, useCount) values(%s, 1)'''
    cur.executemany(sql, newLabels)
    # get all labels' uid, and bound them with bookUid
    sql = '''select uid from bookLabel where name in ''' + labelRange
    num = cur.execute(sql)
    records = cur.fetchmany(num)
    allLabels = [item[0] for item in records]
    sql = '''insert into labelOfBook(bookUid, bookLabelUid) values
          ({}, %s)'''.format(bookUid)
    cur.executemany(sql, allLabels)


    
