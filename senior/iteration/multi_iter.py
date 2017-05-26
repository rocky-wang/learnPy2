# ^_^ coding: utf-8
# 3-6 如何在一个for语句中迭代多个可迭代对象
"""
1、某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，同时
迭代三个列表，计算每个学生的总分。（并行）
2、某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代
每个列表，统计全学年成绩高于90分人数。（人数）
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 通用方案，此案例可行，但当生成器不支持索引方式时，就无法完成
# 解决方案：
# 并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
# 串行：使用标准库中的itertools.chain，它能将多个可迭代对象连接
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from random import randint
from itertools import chain

chinese = [randint(60, 100) for _1 in xrange(10)]
math = [randint(60, 100) for _2 in xrange(10)]
english = [randint(60, 100) for _3 in xrange(10)]

for i in xrange(len(math)):
    print chinese[i] + math[i] + english[i]


a1 = zip([1, 2, 3, 4, 5], ('a', 'b', 'c', 'd'))

print a1

# 总分添加到列表
total = []
for (x, y, z) in zip(chinese, math, english):
    total.append(x + y + z)

# 统计高于90分的
count = 0
for x in chain(chinese, math, english):
    if x > 90:
        count += 1

print 'the higher 90 is %s' % count



