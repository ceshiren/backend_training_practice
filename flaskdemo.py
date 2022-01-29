"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 1、导入Flask 模块
import logging

from flask import Flask
# 2、创建Flask 应用程序的实例
# __name__  == __main__
from backend_demo.log_util import logger

app = Flask(__name__)


# 添加路由
# https://ceshiren.com/search?q=appium
# https ---  协议
# ceshiren.com  --- host 域名
# /search  --- 路由
# ?q=appium   ---- 请求参数
@app.route("/")
def hello_world():
    return "霍格沃兹测试学院"


@app.route("/demo")
def demo():
    return "这是一个demo"


@app.route("/userinfo/<int:username>/")
def hogwarts(username):
    logger.info(f"这是 {username} 同学的个人信息")
    # logging.info(f"这是 {username} 同学的个人信息")
    return f"这是 {username} 同学的个人信息"


# @app.route("/userinfo/<string:username>")
# def hogwarts1(username):
#     return f"这是 {username} 同学的个人信息"

@app.route("/ceshiren")
def ceshiren():
    print("测试人社区.........")
    return "sucess"


# 启动入口
if __name__ == '__main__':
    # flask 服务启动起来，
    # 轮询等待的方式 ，等待浏览器发来请求，
    # 会一直接受请求，直到程序停止
    app.run(host="0.0.0.0", port=5008, debug=True)
