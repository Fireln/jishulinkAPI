import pymysql
import random
from config import Dev


class ConnMysql():

    def __init__(self):
        sql_info = Dev().mysql
        # self.host = host
        self.host = sql_info.get("host")
        self.user = sql_info.get("user")
        self.passwd = sql_info.get("pwd")
        self.base = sql_info.get("base")

    def createconn(self):
        try:
            conn = pymysql.connect(host=self.host, port=3306, user=self.user, passwd=self.passwd,
                                   database=self.base, charset='utf8')
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            return cur, conn
        except Exception as e:
            raise e

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

    def do_insert(self, query):
        try:
            cur, conn = self.createconn()
            cur.execute(query)
            self.closeconn(cur, conn)
        except Exception as e:
            print('查询命令错误', e)

    def do_delete(self, query):
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
    query = r"DELETE FROM tbl_vw_certification_third_record WHERE realname = '周依依'"
    query1 = r"SELECT * FROM tbl_vw_certification_third_record WHERE realname = '周依依'"
    print(con.do_delete(query))
