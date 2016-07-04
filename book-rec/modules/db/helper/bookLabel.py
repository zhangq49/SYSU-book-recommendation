# -*- coding: utf-8 -*-

from modules.db.models.book import BookLabel
from models.db.helper import mysqlConn

@mysqlConn
def getLabels(page=0, size=20, order='useCount', cur, conn):
    if order not in ['useCount']:
        order = 'useCount'
    startIndex = page * size
    sql = '''select name, useCount from bookLabel order by useCount desc 
        limit %s, %s'''
    num = cur.execute(sql, (startIndex, size))
    records = cur.fetchmany(num)
    bookLabels = []
    for rec in records:
        bookLabels.append(BookLabel(rec[0], rec[1]))
    return bookLabels
