"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from sqlalchemy import *
# 导入 Query 以便于调用的时候代码提示
from sqlalchemy.orm import Query

import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 实例化app 对象
from sqlalchemy import *

app = Flask(__name__)
with open("./data.yml") as f:
    result = yaml.safe_load(f)
    username = result.get("database").get('username')
    password = result.get("database").get('password')
    server = result.get("database").get('server')
    db = result.get("database").get('db')
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定app
db = SQLAlchemy(app)


# 定义数据库的表 需要继承 db.Model
class User(db.Model):
    __tablename__ = "user"  # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型，
    # primary_key=True 表示是主键
    id = Column(Integer, primary_key=True)
    # 用户名 不唯一
    username = Column(String(80), nullable=False)
    # email 唯一
    email = Column(String(120), unique=True, nullable=False)
    # email 不唯一
    gender = Column(String(3), nullable=False)

    def __repr__(self):
        return f"<User {self.username}, {self.gender}, {self.email}>"


if __name__ == '__main__':
    # 向数据库中添加 数据
    # db.drop_all()
    # db.create_all()
    # user = User(id=1,username="hogwarts",email='123@123.com',gender="男")
    # print(user)
    # 1、新增表数据，需要导入 User 类，进行实例化
    # user1 = User(username="张三", email="123@123.com",gender="男")
    # # 将数据提交到session
    # db.session.add(user1)
    # # 将数据提交到commit
    # db.session.commit()
    # # 关闭 session
    # db.session.close()

    # 批量添加数据操作
    # user2 = User( username="张四", email="126@123.com",gender="男")
    # user3 = User( username="张五", email="127@123.com",gender="女")
    # # 第一种依次添加，将数据提交到session
    # # db.session.add(user2)
    # # db.session.add(user3)
    # # 第二种批量添加，add_all(列表)
    # db.session.add_all([user2, user3])
    # # 将数据提交到commit
    # db.session.commit()
    # # 端口session
    # db.session.close()

    # 二：查询数据
    # 读取全部数据
    # res = User.query.all()
    # # 遍历数据，得到想要的字段
    # for rs in res:
    #     print(rs.username, rs.email)

    # # 单条数据查询
    # res = User.query.filter_by(gender="男").first()
    # print(res)
    # # 多条数据查询
    # res_all = User.query.filter_by(gender="男").all()
    # print(res_all)

    # # 多条件查询，first()方法只能获取单条数据
    # res = User.query.filter_by(gender="男"). \
    #     filter_by(username='张四').first()
    # print(res)
    # # 多条件查询，all() 获取所有满足条件的数据
    # resal = User.query.filter_by(gender="男"). \
    #     filter_by(username='张四').filter_by(email='aaa@123.com').all()
    # print(resal)

    # 三 ：修改

    # 数据的修改
    # 第一种方式，更新某个字段
    # 先查询出来这条数据对象
    # res = User.query.filter_by(id=2).first()
    # res.gender = "女"
    # # 提交
    # db.session.commit()
    # # 关闭session
    # db.session.close()

    # # 第二种方式，直接调用update方法更新行数据
    # res = User.query.filter_by(id=2).update({"gender": "男"})
    # # 提交
    # db.session.commit()
    # # 关闭session
    # db.session.close()

    # 四：删除数据
    # 方式一：
    # 查询数据
    # user = User.query.filter_by(id=1).first()
    # # 删除操作
    # db.session.delete(user)
    # # 提交
    # db.session.commit()
    # # 关闭session
    # db.session.close()

    # # 方式二：
    # 查询结果直接删除操作
    User.query.filter_by(id=2).delete()
    # 提交
    db.session.commit()
    # 关闭session
    db.session.close()
