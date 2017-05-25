# ^_^ coding: utf-8
# 2-6 如何让字典保持有序
"""
1、某编程竞赛系统，对参赛选手编程解题进行计时，选手完成题目后，
把该选手解题用时记录到字典中，以便赛后按选手名查询成绩。(答题用时越短，成绩越优)
{'LiLei': (2, 43), 'HanMeimei': (5, 52), 'Jim': (1, 39) ...}
比赛结束后，需按排名顺序依次打印选手成绩，如何实现？
"""
# 一般字典是无序排列的，动态添加数据后，内容是无序的
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 使用collections.OrderedDict来替代内置字典Dict
# 依次将选手成绩存入OrderedDict
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()

players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input('go on')
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i+1, p, end - start,
    d[p] = (i+1, end - start)

print
print '_'*20

for k in d:
    print k, d[k]


