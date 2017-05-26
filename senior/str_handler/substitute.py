# coding: utf-8
# 4-3 如何调整字符串中文本的格式
"""
1、某软件的log文件，其中的日期格式为'yyyy-mm-dd'：
......
2017-05-26 10:26:16 status unpacked python3-pip:all
2017-05-26 10:26:16 status half-configured python3-pip:all
2017-05-26 10:26:16 status installed python3-pip:all
2017-05-26 10:26:16 configure python3-wheel:all 0.24.0-1
......
我们想把其中日期改为美国日期的格式'mm/dd/yyyy'
'2017-05-26' => '05/26/2017'，应如何处理？
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# re.sub实际是substitute的缩写，表示替换
# re.sub是个正则表达式方面的函数，用来实现通过正则表达式，实现比普通
# 字符串的replace更加强大的替换功能；
# re.sub共有五个参数：
# 其中三个必选参数：pattern(模式字符串)，repl(被替换)，
# string(表示要被处理，要被替换的那个string字符串)
# 两个可选参数：count, flags
# ---------------------------------------------------
# 解决方案：使用正则表达式re.sub()方法做字符串替换，利用正则表达式
# 的捕获组，捕获每个部分内容，在替换字符串中调整各个捕获组的顺序。
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import re

s1 = "2017-01-22"

c1 = re.compile(u'(\d{4})-(\d{2})-(\d{2})')
c2 = re.compile(u'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')

print re.search(c1, s1).group(2)

res1 = re.sub(c1, r'\2/\3/\1', s1)
res2 = re.sub(c2, r'\g<month>/\g<day>/\g<year>', s1)

print res1
print res2


# 将book.txt中书籍价格提高5%
def func(m):
    price = m.group(2)
    print price
    price = float(price) * 1.05
    return "%s %.2f" % (m.group(1), price)

with open('book.txt') as f:
    # text = f.read()
    text = "booka 12.34 bookb 11.23"
    print re.sub(u'(\w+)\s+(\d+.?\d*)', func, text)
