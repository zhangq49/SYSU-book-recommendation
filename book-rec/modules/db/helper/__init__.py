# -*- coding: utf-8 -*-

from modules.db.config import get_connection, DB

def mysqlConn(func):
    def wrapper(*args):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('USE ' + DB)
        result = func(*args, cur=cur, conn=conn)
        # conn.commit() is execuated by func if needed
        cur.close()
        conn.close()
        return result
    return wrapper
