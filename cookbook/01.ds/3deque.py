# ^_^ coding: utf-8
# 使用deque，传递一个最大值参数，来限制队列大小
#

from collections import deque

pdeque = deque((1, 3, 5), maxlen=6)

pdeque.append(10)
pdeque.appendleft(20)

print pdeque
