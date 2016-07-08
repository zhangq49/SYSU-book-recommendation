# -*- coding: utf-8 -*-

from modules.db.helper import mysqlConn

@mysqlConn
def isDoulieDup(doulieUid, cur, conn):
    sql = '''select uid from doulie where uid = %s'''
    cur.execute(sql, doulieUid)
    record = cur.fetchone()
    return bool(record)

@mysqlConn
def saveDoulieUid(doulieUid, cur, conn):
    sql = '''insert into doulie(uid) values(%s)'''
    cur.execute(sql, doulieUid)
    conn.commit()
