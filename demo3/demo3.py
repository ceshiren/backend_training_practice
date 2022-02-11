"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask, jsonify, render_template, make_response

app = Flask(__name__)

# 返回文本
@app.route('/text')
def get_text():
    return "文本信息"

# 返回元组
@app.route('/tuple')
def tuple_res():
    return "霍格沃兹测试学社",{"hogwarts":"xixi","test":"demo"}

# 返回字典
@app.route('/dict')
def get_dict():
    return {"status":0}

# 返回json
@app.route('/json')
def get_json():
    # return jsonify({"status":0})
    return jsonify(status=1, name="xixi")

# 返回html页面
@app.route('/html')
def get_html():
    return render_template("demo.html")


@app.route('/')
def index():
    resp = make_response(render_template('demo.html'))
    # 设置cookie
    resp.set_cookie('username', 'the username')
    # 设置响应头信息
    resp.headers["hogwarts"] = "ad2"
    return resp

if __name__ == '__main__':
    app.run()