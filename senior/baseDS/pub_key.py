# ^_^ coding: utf-8
# 2-5 如何快速找到多个字典中的公共键(key)
"""
1、西班牙足球甲级联赛，每轮球员进球统计：
第一轮：{'苏亚雷斯': 1, '梅西': 2, '本泽马': 1, 'C罗': 3 ...}
第二轮：{'苏亚雷斯': 2, 'C罗': 3, '格利茨曼': 2, '贝尔': 1 ...}
第三轮：{'苏亚雷斯': 1, '托雷斯': 2, '贝尔': 1, '内马尔': 1 ...}
...
统计出前N轮，没场比赛都有进球的球员。
"""
from random import randint, sample
# 假设abcdefg这7名球员，每场有3-6个球员进球，随机产生人名
soccer_name = 'abcdefg'
# print sample(soccer_name, randint(3, 6))

s1 = {x: randint(1, 4) for x in sample(soccer_name, randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample(soccer_name, randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample(soccer_name, randint(3, 6))}

print s1
print s2
print s3

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 普通方法，迭代第一个对象，然后判断这个对象在后续对象中没有
# 效率非常的低，执行效率不高
# 因为是字典对象，所以in的方式就直接判断key值是否存在
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print res

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 利用集合（set）的交集操作
# step1: 使用字典的viewkeys()方法，得到一个字典keys的集合
# step2: 使用map函数，得到所有字典的keys的集合
# step3: 使用reduce函数，取得所有字典的keys的集合的交集
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print "="*50

r1 = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
print type(r1)
print r1

print reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))

