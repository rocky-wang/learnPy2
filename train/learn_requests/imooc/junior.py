# ^_^ coding: utf-8
# 使用requests的2.17.3版本，
# 利用http://httpbin.org/网站作为测试服务
import requests
import urllib2
import urllib

URL_BASE = 'http://127.0.0.1:8000/get'


def use_simple_requests():
    browse_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, '
                                   'like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    resp = requests.get(URL_BASE, headers=browse_header, params={'name': 'rocky'})
    print resp.text

if __name__ == '__main__':
    use_simple_requests()
