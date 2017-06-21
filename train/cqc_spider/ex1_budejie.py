# ^_^ coding: utf-8
import requests

browse_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36',
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
}

response = requests.get('http://www.budejie.com/text/2', headers=browse_headers)

print response.text

