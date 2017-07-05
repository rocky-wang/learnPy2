# ^_^ coding: utf-8
# heapq是一个堆空间，他最重要的特性是heap[0]代表最小内容，剩余内容可以通过heapq.heappop方法得到
#
import heapq

a1 = [60, 40, 100, 50, 8, 66, 45]

print heapq.nlargest(3, a1)
print a1

heapq.heapify(a1)

print heapq.heappop(a1)


# 实现一个优先级的队列
class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 定义一个商品类
class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{{Item: {!r} }}'.format(self.name)

q = PriorityQueue()
q.push(Item('John'), 1)
q.push(Item('Jim'), 5)
q.push(Item('Lily'), 1)

print q.pop()



