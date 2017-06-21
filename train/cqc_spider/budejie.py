# ^_^ coding: utf-8
import urllib2
import re

request = urllib2.Request('http://www.budejie.com/text/2')

request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/58.0.3029.110 Safari/537.36')

response = urllib2.urlopen(request)

html = response.read()

pattern = re.compile(r'<div class="j-r-list-c-desc">.*?<a.*?href="(.*?)">(.*?)</a>', re.S)
items = pattern.findall(html)

with open('a.txt', 'w') as fp:
    for item in items:
        con_fmt = re.sub('\s*', '', item[1])
        con_fmt = re.sub('<br[/]*?>', '\n', con_fmt)
        buf = "%s:\n\t%s\n\n" % (item[0], con_fmt)
        fp.write(buf)

