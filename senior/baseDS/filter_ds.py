# ^_^ coding: utf-8
# 2-1 如何在列表,字典, 集合中根据条件筛选数据
"""
1、过滤列表中的负数 [3,9,-1,10,20,-2...]
2、筛选出字典中值高于90的项{'LiLei':79, 'Jim':88, 'Lucy':92, ...}
3、筛选出集合中能被3整除的元素{77, 89, 32, 20...}
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 通用做法：迭代 + 判断
# 高级做法：
# ---------------------------------------------------
# | 列表： 使用filter函数或列表解析
#           filter(lambda x: x>=0,data)
#           [x for x in data if x > 0]
# ---------------------------------------------------
# | 字典： 使用字典解析
#           {k:v for k, v in d.iteritems() if v > 90}
#       py3:{k:v for k, v in d.items() if v > 90}
# ---------------------------------------------------
# | 集合： 使用集合解析
#           {x for x in s if x % 3 == 0}
# ---------------------------------------------------
# * 不管是filter还是解析表达式，都是返回一个新的空间，而不会改变
# * 原有空间的值。
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from random import randint
import timeit

"""
* 在python2中产生序列时可以使用xrange方式，他返回的是延迟加载的序列，
    而range方法是直接分配列表空间。
* 在python3中直接使用range方法即可。
"""
# 产生10个-10到10的随机数
t1_lis = [randint(-10, 10) for _ in xrange(10)]
# 产生10个60到100分的用户信息字典
t1_dict = {"S"+str(x): randint(60, 100) for x in xrange(1, 11)}
# 产生一个集合，利用10个数字的列表
t1_set = set(t1_lis)


def filter1_list(li):
    return filter(lambda x: x >= 0, li)


def filter2_list(li):
    return [x for x in li if x >= 0]


def filter1_dict(di):
    return {k: v for (k, v) in di.iteritems() if v >= 90}


def filter1_set(s):
    return {x for x in s if x % 3 == 0}

if __name__ == "__main__":
    print "the list info:", t1_lis
    print filter1_list(t1_lis)
    print timeit.timeit("filter2_list(t1_lis)", setup="from __main__ import filter2_list,t1_lis")
    print "the dict info:", t1_dict
    print filter1_dict(t1_dict)
    print "the set info:", t1_set
    print filter1_set(t1_set)
