#Author : Danea
import pymysql

#获取连接方法
def get_db_conn():
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        db='stu',
        charset='utf8'
    )

    return conn

#查询数据
def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    cur.close()
    conn.close()

    return result

#更改数据库
def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(str(e))

    cur.close()
    conn.close()

#封装常用数据库操作
def check_user(name):
    sql = "select * from student where sname = '{}'".format(name)

    result = query_db(sql)
    return True if result else False

def del_user(name):
    sql = "delete from student where sname='{}'".format(name)
    change_db(sql)

def add_user(id,name,age,sex):
    sql = "insert into student(sid,sname,sage,ssex) values ('{}','{}','{}','{}')".format(id,name,age,sex)
    change_db(sql)