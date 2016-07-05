# -*- coding: utf-8 -*-

from modules.db.models.bookLabel import BookLabel
from modules.db.helper import mysqlConn

@mysqlConn
def getLabels(page=0, size=20, order='useCount', cur=None, conn=None):
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
