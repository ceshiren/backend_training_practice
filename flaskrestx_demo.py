"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
# 1、创建api 实例对象
api = Api(app)


# 2、使用api来添加路由
@api.route('/hello')
# 3、类要继承Resource模块
class HelloWorld(Resource):
    # 4、定义restful 风格的get 方法
    def get(self):
        return {'hello': 'world'}

    # restful 风格的post 方法
    def post(self):
        return {'post': 'true'}


api.add_resource(HelloWorld, '/hello', '/world')

if __name__ == '__main__':
    app.run(debug=True)
