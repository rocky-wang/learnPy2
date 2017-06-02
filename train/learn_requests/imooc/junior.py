# ^_^ coding: utf-8
# 使用requests的2.17.3版本，
import requests

print requests.__version__

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

print r.cookies['example_cookie_name']

print r.text

