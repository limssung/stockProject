import pymysql


def connect():
    Mari.conn = pymysql.connect(host="localhost", port=3306, user='root', password='123123', db='sswdb',
                                charset='utf8')
    Mari.cur = Mari.conn.cursor()


def insert():
    Mari.sql = "CREATE TABLE IF NOT EXISTS USERTABLE(ID VARCHAR(4), USERNAME VARCHAR(20), EMAIL VARCHAR(20), BIRTHYAER INT)"
    Mari.cur.execute(Mari.sql)


def select():
    Mari.sql = "SELECT `DATE`, TOP30, TITLE, RATE, CONTENT, TAGS FROM sswdb.stockdata"
    Mari.cur.execute(Mari.sql)


def disconnect() -> object:
    Mari.conn.commit()
    Mari.conn.close()


class Mari:
    conn = None
    cur = None
    sql = ""
