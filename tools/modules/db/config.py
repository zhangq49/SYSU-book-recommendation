# -*- coding: utf-8 -*-


DEV = True
if DEV:
    HOST = 'localhost'
    PORT = 3306
    USER = 'root'
    PASSWD = 'admin123'
    DB = 'bookrec'


import MySQLdb
def get_connection():
    # print HOST, PORT, USER, PASSWD, DB
    conn = MySQLdb.connect(host = HOST, port = PORT, user = USER, \
        passwd = PASSWD, db = DB, charset = 'utf8')
    return conn
