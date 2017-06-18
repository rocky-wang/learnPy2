# coding: utf-8
import requests
from requests import Request
import json
from rocky_format.format_show import dict_format_show
# base_url = 'https://api.github.com'
base_url = 'http://httpbin.org'


# 连接host信息和资源访问地址，构成URL字符串信息
def build_url(endpoint):
    return '/'.join([base_url, endpoint])


def basic_auth():
    resq1 = requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    resq2 = requests.get('http://httpbin.org/ip')
    dict_format_show(dict(resq2.request.headers))
    dict_format_show(dict(resq2.headers))
    print resq2.status_code


def other_test():
    s = requests.session()
    re1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    dict_format_show(re1.headers)
    re2 = s.get('http://httpbin.org/ip')
    dict_format_show(re2.request.headers)

basic_auth()

