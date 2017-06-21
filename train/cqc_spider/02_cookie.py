# ^_^ coding: utf-8
import urllib2
import urllib
from rocky_format.format_show import dict_format_show
import cookielib

# 申明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# ck_handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# ck_opener = urllib2.build_opener(ck_handler)
# 开启一个连接
# resp = ck_opener.open('http://www.imooc.com/')
#
# dict_format_show(resp.headers.dict)
#
# for item in cookie:
#     print 'Name: ', item.name
#     print 'Value: ', item.value


def login_sys():
    file_name = 'cookie.txt'
    fz_cookie = cookielib.MozillaCookieJar(file_name)
    fz_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(fz_cookie))
    resp = fz_opener.open('http://www.imooc.com/')
    dict_format_show(resp.headers.dict)
    fz_cookie.save(ignore_discard=True, ignore_expires=True)


def login_zh():
    headers = {'User-Agen': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    data1 = {
        '_xsrf': '828e9cd96773e20bf6964d6c607a3c16',
        'password': 'aishila112',
        'phone_num': '13980530592',
        'captcha_type': 'cn'
    }
    post_data = urllib.urlencode(data1)
    request = urllib2.Request('https://www.zhihu.com/login/phone_num', headers=headers, data=post_data)

    file_name = 'cook.txt'
    zh_cookie = cookielib.MozillaCookieJar(file_name)
    zh_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(zh_cookie))

    resp = zh_opener.open(request)
    print resp.code
    print resp.read()
    zh_cookie.save(ignore_discard=True, ignore_expires=True)

login_zh()




