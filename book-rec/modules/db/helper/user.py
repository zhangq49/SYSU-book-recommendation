# -*- coding: utf-8 -*-

from modules.db.helper import mysqlConn
from modules.db.helper import book as bookHelper

@mysqlConn
def saveUser(userToken, cur, conn):
    '''Save user's token into database.

    It's the caller's reponsibility to make sure that the userToken is not
    duplicate.
    '''
    sql = '''insert into user(token, recBooks) values(%s, %s)'''
    recBooks = bookHelper.getPopularBooks(20)
    recBookUids = [str(book.uid) for book in recBooks]
    booksStr = ','.join(recBookUids)
    cur.execute(sql, (userToken, booksStr))
    conn.commit()
