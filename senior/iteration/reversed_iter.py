# ^_^ coding: utf-8
# 3-4 如何进行反向迭代以及如何实现反向迭代？
"""
1、实现一个连续浮点数发生器FloatRange(和xrange类似)，根据给定
范围(start, end)和步进值(step)产生一些列连续浮点数，如迭代
FloatRange(3.0, 4.0, 0.2)可产生序列：
正向：3.0 -> 3.2 -> 3.4 -> 3.6 -> 3.8 -> 4.0
反向：4.0 -> 3.8 -> 3.6 -> 3.4 -> 3.2 -> 3.0
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 方法1，如果使用列表本身的reverse函数的话，会导致改变原数据
# 方法2，使用倒序切片方法，属于拷贝一个一样的空间，浪费空间
# 建议方法： reversed得到列表的反向迭代器
# 使用reversed方法，其实是调用对象的__reversed__方法
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from collections import Iterable

ltest1 = [1, 3, 4, 7, 11, 18]

# ltest1.reverse()
a1 = ltest1[::-1]

print ltest1
print a1

for item in reversed(ltest1):
    print item

print '_'*50


# 定义FloatRange类型
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        val = self.start
        while val <= self.end:
            yield val
            val += self.step

    def __reversed__(self):
        val = self.end
        while val >= self.start:
            yield val
            val -= self.step

f01 = FloatRange(1.0, 4.5, 0.3)

for item in reversed(f01):
    print item
