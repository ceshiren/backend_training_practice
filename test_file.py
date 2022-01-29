"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests


def test_file():
    url = "http://127.0.0.1:5000/file"
    file = {'file': open("/Users/juanxu/Downloads/logo.jpg", 'rb')}
    r = requests.post(url, files=file)
    assert r.status_code == 200
