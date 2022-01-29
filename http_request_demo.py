"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask

app = Flask(__name__)


# methods 是一个列表类型，可以添加多种 请求方式 ，get, post, put,delete...
@app.route("/cases", methods=["get"])
def get_case():
    return {"code": 0, "msg": "get success"}


@app.route("/cases", methods=["post"])
def post_case():
    return {"code": 0, "msg": "post success"}


# put 请求
@app.route("/cases", methods=["put"])
def put_case():
    return {"code": 0, "msg": "put success"}


# delete 请求
@app.route("/cases", methods=["delete"])
def delete_case():
    return {"code": 0, "msg": "delete success"}


if __name__ == '__main__':
    app.run()
