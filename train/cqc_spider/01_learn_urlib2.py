# ^_^ coding: utf-8
import urllib2
from rocky_format.format_show import dict_format_show
import re
import urllib


def get_charset(s):
    pattern = re.compile('charset=(.*)')
    ct1 = pattern.search(s)
    if ct1:
        return ct1.group(1)
    else:
        return None


class Httpdown:
    def __init__(self, turl, encode='utf-8', fn=None):
        self.web_url = turl
        self.browse_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                            "like Gecko) Chrome/58.0.3029.81 Safari/537.36"}
        self.encode = encode
        self.file_name = fn

    def get_page(self, method='GET'):
        request = urllib2.Request(self.web_url, headers=self.browse_header)
        request.get_method = lambda: method
        try:
            resp = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            print 'http error: ', e.code
        except urllib2.URLError as e:
            print 'url error', e.reason
        else:
            print 'success'
            dict_format_show(resp.headers.dict)
            cnt = resp.headers.dict.get('content-type', None)
            dcode = None
            if cnt:
                dcode = get_charset(cnt)
            buf = resp.read()
            if self.file_name:
                with open(self.file_name, 'wb') as fp:
                    fp.write(buf)
            else:
                if dcode:
                    print buf.decode(dcode).encode('utf-8')
                else:
                    print buf

if __name__ == '__main__':
    # get_charset('text/html; charset=GB2312')
    task1 = Httpdown('http://www.5566.net')
    task1.get_page(method='PUT')
