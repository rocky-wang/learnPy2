# ^_^ coding: utf-8
# 4-5 如何对字符串进行左, 右, 居中对齐
"""
1、某个字典存储了一系列属性值，
{
    "loadDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}
在程序中，我们想以以下工整的格式将其内容输出，如何处理？
SmallCull : 0.04
farclip   : 477
....
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 方法一： 使用字符串的str.ljust(), str.rjust(), str.center()进行左，右，居中对齐。
# 方法二： 使用format()方法，传递类似'<20','>20','^20'参数完成同样任务。
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

d = {'Adddd': 500.0, 'sB': 0.04, 'qqqqqqqqqqC': 477, 'Dddd': 100.0, 'E': 40}
# 正常迭代的话
for i in d:
    print i, ':', d[i]

s = 'abc'
r1 = s.center(20, '=')

print r1

print "{a:=<20}".format(a=s)

print format(s, '=>20')

a1 = map(len, d.viewkeys())
print a1
max_len = max(a1)

fo = "{k:<%d}: {v}" % max_len

for y in d:
    # print y.ljust(max_len), ': ', d[y]
    # print fo.format(k=y, l=max_len, v=d[y])
    print ("{k:<%d}: {v}" % max_len).format(k=y, v=d[y])

