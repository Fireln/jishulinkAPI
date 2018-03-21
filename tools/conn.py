import pymysql
import random
from setting import MySql
import exceptions


class ConnMysql():

    def __init__(self):
        # self.host = host
        self.host = MySql.host
        self.port = MySql.port
        self.user = MySql.user
        self.passwd = MySql.passwd
        self.base = MySql.base

    def createconn(self):
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                                   database=self.base)
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            return cur, conn
        except exceptions.OdbcError as e:
            raise exceptions.OdbcError("connect sql error")

    def do_select(self, query):
        try:
            cur, conn = self.createconn()
            cur.execute(query)
            ret = self.processres(cur)
            self.closeconn(cur, conn)
            return ret
        except Exception as e:
            print('查询命令错误', e)

    def do_update(self, query, database):
        try:
            cur, conn = self.createconn()
            cur.execute(query)
            self.processres(cur)
            self.closeconn(cur, conn)
        except Exception as e:
            print('查询命令错误', e)

    def do_insert(self, query, database):
        try:
            cur, conn = self.createconn()
            cur.execute(query)
            self.closeconn(cur, conn)
        except Exception as e:
            print('查询命令错误', e)

    def do_delete(self, query, database):
        try:
            cur, conn = self.createconn()
            cur.execute(query)
            conn.commit()
            self.closeconn(cur, conn)
        except Exception as e:
            print('删除命令错误', e)

    def processres(self, cur):
        rows = cur.fetchall()
        l = []
        for i in rows:
            l.append(i)
        return l

    def closeconn(self, cur, conn):
        cur.close()
        conn.close()


if __name__ == '__main__':
    con = ConnMysql()
    query = r"SELECT user_id FROM  tbl_vw_user WHERE telephone LIKE  '170%' LIMIT 0, 200"
    print(con.do_select(query))
