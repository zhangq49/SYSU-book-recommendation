# -*- coding: utf-8 -*-

from modules.env import DEV

if DEV:
    HOST = 'localhost'
    PORT = 3306
    USER = 'root'
    PASSWD = 'admin123'
    DB = 'bookrec'
else:
    import sae.const
    HOST = sae.const.MYSQL_HOST
    PORT = int(sae.const.MYSQL_PORT)
    USER = sae.const.MYSQL_USER
    PASSWD = sae.const.MYSQL_PASS
    DB = sae.const.MYSQL_DB

import MySQLdb
def get_connection():
    # print HOST, PORT, USER, PASSWD, DB
    conn = MySQLdb.connect(host = HOST, port = PORT, user = USER, \
        passwd = PASSWD, db = DB, charset = 'utf8')
    return conn
