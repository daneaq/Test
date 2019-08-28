#Author : Danea

import pymysql
import configparser

#读取配置文件

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')
host = config.get('mysql','host')
port = config.get('mysql','port')
user = config.get('mysql','user')
passwd = config.get('mysql','passwd')
db = config.get('mysql','db')
charset = config.get('mysql','charset')

print(host,port,user,passwd,db,charset)


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db
                # charset=charset
            )

    def __del__(self):
        # self.cur.close()
        self.conn.close()

    # def query_db(self,sql):
    #     self.cur.execute(sql)
    #     return self.cur.fetchall()

    def exec(self,comm,sql):
        self.cur = self.conn.cursor()

        if comm in ['select','SELECT']:
            self.cur.execute(sql)
            return self.cur.fetchall()
        elif comm in ['update','UPDATE','delete','DELETE','insert','INSERT']:
            try:
                self.cur.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(str(e))
        else:
            print("command error")



    def check_uer(self,name):
        sql="select * from student where sname={}".format(name)
        result = self.exec('select',sql)

    def add_user(self,sid,sname,sage,ssex):
        sql = "insert into student(sid,sname,sage,ssex) values ('{}','{}','{}','{}')".format(sid,sname,sage,ssex)
        self.exec('insert',sql)

    def del_user(self,name):
        sql = "delete from student where sname='{}'".format(name)
        self.exec('delete',sql)

db = DB()
print(db.check_uer("张美丽"))