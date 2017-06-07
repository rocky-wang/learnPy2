# ^_^ coding: utf-8
# 使用多线程进行爬取
import threading
import urllib2
import re
import os


class SpiderThreadMzRegex(threading.Thread):
    # 构造方法
    def __init__(self, root_url, pattern, deep_index=1, file_path='./'):
        # 爬取的根url地址信息
        super(SpiderThreadMzRegex, self).__init__()
        self.url = root_url
        # 爬虫伪造浏览器user-agent
        self.browse_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                            "like Gecko) Chrome/58.0.3029.81 Safari/537.36"}
        # 根据传递的file_path进行保存信息解析
        self.saved_info = {"dir_name": "./", "file_name": "", "gen": True}
        self.analysis_file_name(file_path)
        # 解析爬取深度
        self.deep = 1
        if deep_index > 1:
            self.deep = deep_index
        # 判断URL是否具备深度格式
        if self.url.index('%s'):
            # 说明可以进行深度遍历获取数据
            self.flag = 1
        else:
            self.flag = 0
        # 获取正则表达式
        self.regex = pattern

    # 解析保存文件的内容信息
    def analysis_file_name(self, file_path):
        size = len(file_path)
        if size == 0:
            return None
        # 传入的是目录，那么文件名自动生成
        if file_path[size - 1] == '/' or file_path[size - 1] == '\\':
            if not os.path.isdir(file_path):
                os.makedirs(file_path)
            self.saved_info['dir_name'] = file_path
            self.saved_info['gen'] = True

    # 解析内容写入文件
    @staticmethod
    def gain_data(buf, pattern, file_path):
        items = re.findall(pattern, buf)
        if len(items) == 0:
            return None
        with open(file_path, 'w') as fp:
            for item in items:
                con_fmt = re.sub('\s*', '', item[1])
                con_fmt = re.sub('<br[/]*?>', '\n', con_fmt)
                buf = "%s:\n\t%s\n\n" % (item[0], con_fmt)
                # fp.write(buf.decode('utf-8').encode('gb2312'))
                fp.write(buf)

    # *获取网页源代码，并保存到文件*
    def get_page_index(self, index):
        if self.flag:
            page_url = self.url % index
        else:
            page_url = self.url
        # 更新文件名
        req = urllib2.Request(page_url, headers=self.browse_header)
        if self.saved_info.get('gen'):
            self.saved_info['file_name'] = '%s_%s.txt' % (req.get_host()[4:8], index)

        try:
            resp = urllib2.urlopen(req)
            content = resp.read()
            self.gain_data(content, self.regex, '%s%s' % (self.saved_info['dir_name'], self.saved_info['file_name']))
        except urllib2.HTTPError as e:
            print 'HTTPError: ', e.code,
            if hasattr(e, 'reason'):
                print e.reason
            return None
        except urllib2.URLError as e:
            print 'URLError: ', e.reason
            return None
        else:
            return "success"

    # 开始爬取
    def run(self):
        print threading.current_thread().name
        res = self.get_page_index(self.deep)
        if res:
            print threading.current_thread().name, 'get', self.deep, 'success'
        else:
            print threading.current_thread().name, 'get', self.deep, 'failed'

if __name__ == '__main__':
    url = 'http://www.maiziedu.com/course/teachers/?page=%s'
    baike_regex = re.compile('li class="t3out".*?p">(.*?)<.*?简介：</span>(.*?)</p>', re.S)
    thread_pool = []
    for x in xrange(5):
        spy = SpiderThreadMzRegex(url, baike_regex, deep_index=x+1, file_path='./bak/')
        spy.start()
        thread_pool.append(spy)

    for i in thread_pool:
        i.join()
    print '+++++success+++++'
