# coding: utf-8
# 3-3 如何使用生成器函数实现可迭代对象
"""
实现一个可迭代对象的类，它能迭代出给定范围内所有素数
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 1、将该类的__iter__方法实现成生成器函数，每次yield返回一个元素
# --------------------------------------------------
# 当函数里出现yield时，该函数会自动编译为生成器，当函数调用时，
# 相当于增加了一个__iter__方法的对象就返回了
# 生成器对象既实现可迭代接口又生成迭代器接口，他返回的就是他自身
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from collections import Iterable, Iterator


def f():
    print 'in f(), 1'
    yield 1
    print 'in f(), 2'
    yield 2
    print 'in f(), 3'
    yield 3

g = f()

print dir(g)
print isinstance(g, Iterator)
print g.__iter__() is g


def check_primer(num):
    if num < 2:
        return False
    for i in xrange(2, num):
        if num % i == 0:
            return False
    return True


class PrimerNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if check_primer(k):
                yield k

for x in PrimerNumbers(1, 100):
    print x,


def gen_primer(start, end):
    for k in range(start, end):
        if check_primer(k):
            yield k
    raise StopIteration

for y1 in gen_primer(1, 100):
    print y1

