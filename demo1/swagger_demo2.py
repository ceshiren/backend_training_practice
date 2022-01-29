"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask, request
from flask_restx import Resource, Api, Namespace, fields
from werkzeug.datastructures import FileStorage

from backend_demo.demo.log_util import logger

app = Flask(__name__)
api = Api(app)
hello_ns = Namespace("demo", description="demo学习")


@hello_ns.route("")
class Demo(Resource):
    # 定义parser解析器对象
    get_parser = api.parser()
    # 通过 Parser对象添加测试参数
    # required 是否为必填项 ，True为必填
    get_parser.add_argument('id', type=int, location="args", required=True)
    get_parser.add_argument('case_title', type=str, location="args", required=True)

    @hello_ns.expect(get_parser)
    def get(self):
        logger.info(f"request.args ===>{request.args}")
        return {"code": 0, "msg": "get success"}

    post_parser = api.parser()
    # location 要与request 对象属性对应
    # post_parser.add_argument("file",type=FileStorage,location="files")
    # post_parser.add_argument("param1",help="username",type=str,location="form")
    # post_parser.add_argument("param2",help="password",type=int,location="form")
    post_parser.add_argument("choice", choices=("one", "two"), location="args")
    post_parser.add_argument("id", type=int, location="json", required=True)
    post_parser.add_argument("casetitle", type=str, location="json", required=True)

    @hello_ns.expect(post_parser)
    def post(self):
        # logger.info(f"request.json===>{request.files}")
        # logger.info(f"request.json===>{request.form}")
        logger.info(f"request.json===>{request.args}")
        return {"code": 0, "msg": "post success"}


api.add_namespace(hello_ns, "/hello")

if __name__ == '__main__':
    app.run(debug=True)
