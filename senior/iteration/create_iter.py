# coding: utf-8
# 3-1 如何实现可迭代对象和迭代器对象(1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# for循环的背后，确保in后边为可迭代对象，因为in会自动将后面对象进行iter()升级
# 可迭代对象可以由内置函数iter得到一个迭代器对象
# 注意：可迭代和迭代器对象概念区别，不要混淆
# iterable：需要实现__iter__或者__getitem__接口
# itertor：需要实现next方法，访问时只能通过next()获取数据
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from itertools import islice
l = [1, 2, 3, 4]
s = "abcde"

print hasattr(l, "__iter__")
print hasattr(s, "__iter__")
print hasattr(s, "__getitem__")


# 定义一个具有迭代性的类型
class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    # def __getitem__(self, item):
    def __iter__(self):
        print '...iter...'
        return self

    def next(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

n1 = Fib()
in1 = iter(n1)

print in1
print in1.next()
print in1.next()
print in1.next()

print list(islice(n1, 0, 10))

