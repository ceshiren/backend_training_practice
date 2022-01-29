"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
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


# 定义数据库的表 需要继承 db.Model，db 为 app 启动的时的 SQLAlchemy 绑定的实例
# 类名，相当于表名
class UserInfo(db.Model):
    # 指定表名__tablename__属性
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(80))


class StudentsInfo(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    gender = Column(String(80))


if __name__ == '__main__':
    # 创建表
    db.create_all()
    # 删除表
    # db.drop_all()
