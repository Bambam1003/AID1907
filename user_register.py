"""
用户注册和登录的模拟实现
包装成类
"""
import pymysql


class User(object):

    def __init__(self):
        self.db = pymysql.connect(user='root',
                                  password='123456',
                                  database='stu')
        self.cur = self.db.cursor()

    def name_pwd(self):
        id = input("请输入你的用户id：")
        password = input("请输入你的密码：")
        re_password = input("请确认你的密码：")
        if password == re_password:
            return id, password
        else:
            print("密码确认不正确！")

    def register(self):
        while True:
            result = self.name_pwd()
            if result:
                sql = "select * from user WHERE id = %s"
                self.cur.execute(sql, [result[0]])
                re = self.cur.fetchall()
                if re:
                    print("用户名已存在")
                    continue
                else:
                    sql = "insert into user VALUES (%s, %s)"
                    self.cur.execute(sql, [result[0], result[1]])
                    self.db.commit()
                    return True

    def login(self):
        id = int(input("请输入用户名："))
        password = int(input("请输入你的密码："))
        sql = "select * from user where id = %s and password = %s"
        self.cur.execute(sql, [id, password])
        re = self.cur.fetchall()
        if re:
            return True


if __name__ == '__main__':
    user = User()
    # if user.register():
    #     print("注册成功")
    if user.login():
        print("登录成功")




