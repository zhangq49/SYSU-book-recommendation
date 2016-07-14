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

@mysqlConn
def getAllLabels(cur, conn):
    sql = '''select name from bookLabel'''
    num = cur.execute(sql)
    records = cur.fetchmany(num)
    nameList = [rec[0] for rec in records]
    nameSet = set(nameList)
    # print len(nameList), len(nameSet)
    return list(nameSet)

@mysqlConn
def clearDupLabel(cur, conn):
    allLabels = getAllLabels()
    for label in allLabels:
        validLabel = getValidLabel(label, cur, conn)
        # allDupId = getAllDupId(validLabel[0], cur, conn) 
        try:
            copyLabel(validLabel, cur, conn)
        except Exception, e:
            continue
        copyLabelRelation(validLabel[0], cur, conn)
    conn.commit()
            

def isDup(label, cur, conn):
    sql = '''select count(*) from bookLabel where name = %s'''
    cur.execute(sql, label)
    if cur.fetchone()[0] == 1:
        return False
    else:
        return True

def getValidLabel(label, cur, conn):
    sql = '''select uid, name, useCount from bookLabel where name = %s 
             order by useCount desc limit 1'''
    cur.execute(sql, label)
    return cur.fetchone()

def copyLabel(validLabel, cur, conn):
    print validLabel[0], validLabel[1], validLabel[2]
    sql = '''insert into bookLabel2(uid, name, useCount) values(%s, %s, %s)'''
    cur.execute(sql, validLabel)

def copyLabelRelation(labelId, cur, conn):
    sql = '''select bookUid, bookLabelUid from labelOfBook
             where bookLabelUid = %s'''
    num = cur.execute(sql, labelId)
    records = cur.fetchmany(num)
    #
    sql = '''insert into labelOfBook2(bookUid, bookLabelUId) values(%s, %s)'''
    cur.executemany(sql, records)


if __name__ == '__main__':
    clearDupLabel()