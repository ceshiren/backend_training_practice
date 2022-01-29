"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask
from flask_restx import Resource, Api, Namespace, fields

app = Flask(__name__)
api = Api(app, version="2.0")
hello_ns = Namespace("demo", description="demo学习")


@hello_ns.route("")
class Demo(Resource):
    # restful 风格的 get 方法
    @hello_ns.doc(params={'id': 'An ID'}, required=True)
    def get(self):
        return {"code": 0, "msg": "get success"}

    post_model = api.model('PostModel', {
        # required 约束，是否为必填项
        'name': fields.String(description='The name', required=True),
        # enum 枚举类型,只允许在这给定的值里面使用
        'type': fields.String(description='The object type', enum=['A', 'B']),
        # min 允许的最小值 为0
        'age': fields.Integer(min=0),
    })

    # restful 风格的 post 方法
    @hello_ns.doc(body=post_model)
    # @hello_ns.expect(post_model)
    def post(self):
        return {"code": 0, "msg": "post success"}


api.add_namespace(hello_ns, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
