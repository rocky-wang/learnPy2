# coding: utf-8
import requests
import base64
# base_url = 'http://httpbin.org'
base_url = 'https://api.github.com'


# 格式化打印字典信息
def dict_format_show(data):
    keys_len = map(len, data.viewkeys())
    max_len = max(keys_len) + 1
    fo = "{k:<%d}: {v}" % max_len
    for y in data:
        print fo.format(k=y, v=data[y])


# 连接host信息和资源访问地址，构成URL字符串信息
def build_url(endpoint):
    return '/'.join([base_url, endpoint])


def basic_auth():
    resp = requests.get(build_url('ip'), auth=('rocky', 123))
    print '>'*20, 'request headers: ', '>'*20
    dict_format_show(dict(resp.request.headers))
    # print dict(resp.request.headers)
    print '>'*20, 'response headers: ', '>'*20
    dict_format_show(dict(resp.headers))


def basic_oauth():
    oauth = {'Authorization': 'token e048129911767ea90f6fef8045bdee30371efd09'}
    resp = requests.get(build_url('user/emails'), headers=oauth)
    dict_format_show(dict(resp.request.headers))
    print resp.text

if __name__ == '__main1__':
    basic_auth()
    infs = base64.b64decode('cm9ja3k6MTIz')
    de_infs = base64.b64encode('rocky:123')
    print infs
    print de_infs

if __name__ == '__main__':
    basic_oauth()
