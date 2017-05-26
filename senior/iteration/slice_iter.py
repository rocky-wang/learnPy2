# ^_^ coding: utf-8
# 3-5 如何对迭代器做切片操作
"""
1、有某个文本文件，我们想读取其中某范围的内容如100 ~ 300行之间的内容，
python中文本文件是可迭代对象，我们是否可以使用类似列表切片的方式得到
一个100 ~ 300行文件内容的生成器？
f = open('/var/log/dmesg')
f[100:300]
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案： 使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器
# 要进行切片，实际就是调用__getitem__方法
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from itertools import islice


class Mydef:
    def __init__(self, val=10):
        self.val = val

    def __getitem__(self, item):
        print 'get item...'
        print item
        return self.val

n1 = Mydef()

print n1[1:3]
print n1[1:]
print n1[1]

# print islice.__doc__

with open('../baseDS/CodingStyle') as f:
    for line in islice(f, 100, 150):
        print line


