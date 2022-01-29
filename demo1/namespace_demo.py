"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask
from flask_restx import Resource, Api, Namespace

app = Flask(__name__)
api = Api(app)
# 定义了两个命名空间
hello_ns = Namespace("demo", description="demo学习")
case_ns = Namespace("case", description="用例管理")


# 接口路径定义到类上，对应的不同请求操作创建不同的方法
# 将@api.route("/case")   改为 @case_ns.route("")
# @case_ns.route("")定义子路由，如果没有的话，就传空字符串即可""
@case_ns.route("")
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


@hello_ns.route("")
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


api.add_namespace(hello_ns, '/hello')
api.add_namespace(case_ns, '/case')

if __name__ == '__main__':
    app.run(debug=True)
