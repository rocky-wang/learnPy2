# coding: utf-8
# 爬取糗事百科的文字内容，并保存到文件中
import urllib2
import re
import os


def gain_data(buf, pattern, dir_name):
    items = pattern.findall(buf)
    if len(items) == 0:
        return None
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    with open(dir_name+'teq.txt', 'w') as fp:
        # 扩展：使用命名元组
        for item in items:
            con_fmt = re.sub('\s*', '', item[1])
            con_fmt = re.sub('<br[/]*?>', '\n', con_fmt)
            buf = "%s:\n\t%s\n\n" % (item[0], con_fmt)
            fp.write(buf)
    return 1


def get_data_from_pattern(url, dir_name='.'):
    browse_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                   "Chrome/58.0.3029.81 Safari/537.36"}
    req = urllib2.Request(url, headers=browse_header)
    try:
        resq = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print 'http error:', e.code,
        if hasattr(e, 'reason'):
            print e.reason
        return None
    except urllib2.URLError as e:
        print 'url error:' + e.reason
        return None
    else:
        content = resq.read()
        # baike_regex = re.compile("<a href=\"/article/(\d+?)\"\w*?class='contentHerf'>\w*?<span>(\w*?)</span>")
        baike_regex = re.compile("href=\"/article/(\d+?)\".*?class='contentHerf'.*?<span>(.*?)</span>", re.S)
        gain_data(content, baike_regex, dir_name)
    return "success save %s" % dir_name

if __name__ == '__main__':
    root_url = 'https://www.qiushibaike.com/text/'
    # root_url = 'http://www.5566.net/'
    save_dir = './bak/'

    info = get_data_from_pattern(root_url, dir_name=save_dir)
    if not info:
        print "failed"
    else:
        print info
