# ^_^ coding: utf-8
# 2-3 如何统计序列中元素的出现频率？
"""
1、某随机序列[12, 5, 6, 4, 6, 5, 5, 7,...]中，
找到出现次数最高的3个元素，他们出现次数是多少？
2、对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，
他们出现次数是多少？
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 普通方法：
# 1、先产生一个字典，用随机数作为key值
# 2、遍历随机数，将key值相同的累加
# 3、排序输出
# ---------------------------------------------------
# 高级方法：
# 使用collections.Counter，将序列传入Counter的构造器
# 得到Counter对象是元素频度的字典。
# Counter.most_common(n)方法得到频度最高的n个元素的列表
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from random import randint
from collections import Counter
import re
# 产生30个随机数，随机数访问0-15，这样必然会有重复数据
r1_seq = [randint(0, 15) for _ in xrange(30)]


def common_statistic(r_seq):
    # 创建字典，根据源数据
    d1 = dict.fromkeys(r_seq, 0)
    for x in r_seq:
        d1[x] += 1
    res = sorted(d1.items(), key=lambda item: item[1], reverse=True)
    print type(res)
    print res


def collect_statistic(r_seq):
    c2 = Counter(r_seq)
    print type(c2)
    print c2.most_common(3)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 统计单词频率
# 利用CodingStyle这篇文章，使用正则表达式进行内容过滤
# 使用re.split对文章单词进行分离，然后交给Counter进行统计
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def statistic_file(file_name):
    with open(file_name) as fp:
        txt = fp.read()
    c2 = Counter(re.split('\W+', txt))
    print c2.most_common(10)

if __name__ == "__main__":
    print r1_seq
    common_statistic(r1_seq)
    collect_statistic(r1_seq)
    statistic_file('CodingStyle')


