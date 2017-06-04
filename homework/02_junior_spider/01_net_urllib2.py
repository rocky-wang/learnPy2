# coding: utf-8
# 使用urllib2来进行http协议的数据交互，通过使用urllib的encode进行数据头信息的编码
# 建议编写流程：构造Request请求头数据，urlopen发送请求并接收响应respone。
# respone常用的方法：
# resq.close     resq.fp        resq.headers   resq.next      resq.readlines
# resq.code      resq.getcode   resq.info      resq.read      resq.url
# resq.fileno    resq.geturl    resq.msg       resq.readline
import urllib2
import urllib

if __name__ == '__main__':
    turl1 = 'http://www.5566.net'
    browse_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                   "Chrome/58.0.3029.81 Safari/537.36"}
    values = {'user': 'jim', 'pwd': '123456'}
    content = urllib.urlencode(values)
    flags = 1

    if flags:
        # GET请求
        turl1 = "%s?%s" % (turl1, content)
        req = urllib2.Request(turl1, headers=browse_header)
    else:
        # POST请求
        req = urllib2.Request(turl1, headers=browse_header, data=content)

    try:
        resq = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print e.code
        if hasattr(e, 'reason'):
            print e.reason
    except urllib2.URLError as e:
        print e.reason
    else:
        print "success"
        buf = resq.read()
        with open('tmp.txt', 'w') as fp:
            # 原网页是GB2312编码，现转换为UTF-8进行存储本地
            fp.write(buf.decode('gb2312').encode('utf-8'))

    str1 = '你好'
    print type(str1.decode('utf-8'))
