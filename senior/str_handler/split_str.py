# coding: utf-8
# 4-1 如何拆分含有多种分隔符的字符串
"""
1、我们要把某个字符串依据分隔符号拆分不同的字段，该字符串
包含多种不同的分隔符，例如：
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
其中, ; | \t都是分隔符号，如何处理？
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 案例1，只有一种分隔符，直接使用str.split即可
# 解决方案：
# 1、连续使用str.split()方法，每次处理一种分隔符号
# 2、使用正则表达式的re.split()方法，一次性拆分字符串
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import re
s1 = 'rocky Jim 1.0 2.0 3.0 R+'
stest = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'

print s1.split(' ')


def my_split(s, ds):
    res = [s]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    # 改进，过滤非空字符串
    return [y for y in res if y]

print my_split(stest, ";,|\t")

res1 = re.split(r'[,;\t|]+', stest)
print res1
