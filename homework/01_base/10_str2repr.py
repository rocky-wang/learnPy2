# ^_^ coding: utf-8
# 比较str和repr的区别，一般来说，str返回对用户友好的字符串，repr返回对程序空间友好的内容

a1 = 3.14
s1 = 'hello world'

print str(s1)
print repr(s1)

print str(a1)
print repr(a1)

print s1[::-1]


class MyItem(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print 'in str'
        return 'Myitem{0}'.format(self.name)

    def __repr__(self):
        print 'in repr'
        return 'Myitem: {iid} is {n}'.format(iid=id(self.name),n=self.name)

b1 = MyItem('ro')

print repr(b1)
