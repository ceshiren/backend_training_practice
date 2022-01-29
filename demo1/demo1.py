"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


# 接口路径定义到类上，对应的不同请求操作创建不同的方法

@api.route("/case")
class TestCase(Resource):
    # restful 风格的 get 方法
    def get(self):
        return {"code": 0, "msg": "get success"}

    # restful 风格的 post 方法
    def post(self):
        return {"code": 0, "msg": "post success"}

    # restful 风格的 put 方法
    def put(self):
        return {"code": 0, "msg": "put success"}

    # restful 风格的 delete 方法
    def delete(self):
        return {"code": 0, "msg": "delete success"}


@api.route("/demo")
class Demo(Resource):
    # restful 风格的 get 方法
    def get(self):
        return {"code": 0, "msg": "get success"}

    # restful 风格的 post 方法
    def post(self):
        return {"code": 0, "msg": "post success"}

    # restful 风格的 put 方法
    def put(self):
        return {"code": 0, "msg": "put success"}

    # restful 风格的 delete 方法
    def delete(self):
        return {"code": 0, "msg": "delete success"}


if __name__ == '__main__':
    app.run(debug=True)
