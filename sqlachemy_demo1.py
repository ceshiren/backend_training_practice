"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 导入Flask的类
from flask import Flask
# 实例化 Flask的类，并且绑定module
from flask_sqlalchemy import SQLAlchemy

# 实例化 Flask
app = Flask(__name__)

# mysql 数据库用户名
username = "root"
# mysql 数据库密码
pwd = "123456"
# mysql 数据库的 host 地址
ip = "127.0.0.1"
# mysql 数据库端口
port = "3306"
# 代码使用的数据库名
database = "demo"

# 设置mysql 链接方法是
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'

# 定义应用使用数据库的配置
# 设置SQLALCHEMY_TRACK_MODIFICATIONS参数 不设置该配置的时候会抛出警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 将 app 与 Flask-SQLAlchemy 的 db 进行绑定
db = SQLAlchemy(app)
