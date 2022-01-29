"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 需要导入 request 对象，不是 requests!!!!!
from flask import Flask, request

from backend_demo.log_util import logger

app = Flask(__name__)


@app.route("/login/", methods=["get"])
def login():
    logger.info(f"请求参数为：{request.args}")
    result = request.args
    a = result.get("a")
    b = result.get("b")
    print(f"a = {a} , b ={b}")
    return {"code": 0, "msg": "get success"}


@app.route("/regist/", methods=["post"])
def post_regist():
    logger.info(request.json)
    return {"code": 0, "msg": "post success"}


# 处理前端发来的form表单请求
# 注册，用户名，密码,确定密码，邮箱
@app.route("/regist1/", methods=["put"])
def regist1():
    name = request.form.get("name")
    password = request.form.get("passwd")
    password_confirm = request.form.get("passwd_confirm")
    email = request.form.get("email")
    logger.info(request.form)
    logger.info(f"注册的用户信息为：name:{name},  password:{password}, password_confirm: {password_confirm}, email :{email}")

    return {"code": 0, "msg": "put success"}


# 处理前端发来的文件请求
@app.route("/file/", methods=["post"])
def post_file():
    logger.info(f"请求的方式为：{request.method}")
    logger.info(f"请求的URL为：{request.url}")
    fileobj = request.files.get("file")
    logger.info(fileobj)
    filename = fileobj.filename
    logger.info(f"文件名为：{filename}")
    fileobj.save("./logo1.png")
    return {"code": 0, "msg": "post success"}


if __name__ == '__main__':
    app.run()
