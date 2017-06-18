# coding: utf-8
import requests


def download_image():
    img_url = 'https://i2.wp.com/coding.memory-forest.com/wp-content/uploads/2011/07/github.png?resize=300%2C300'
    resp = requests.get(img_url)

    print resp.status_code, resp.reason
    print resp.headers

    with open('demo.png', 'wb') as fd:
        for chunk in resp.iter_content(128):
            fd.write(chunk)


def getstream():
    r = requests.get('https://github.com/timeline.json', stream=True)
    print r.raw
    buf = r.raw.read(20)
    print type(buf)

getstream()
