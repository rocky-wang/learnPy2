# ^_^ coding: utf-8
# 4-6 如何去掉字符串中不需要的字符
"""
1、过滤掉用户输入中前后多余的空白字符: '  nick2008@gmail.com'
2、过滤某windows下编辑文本中的'\r': 'hello world\r\n'
3、去掉文本中的unicode组合符合（音调）:
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 方法一： 字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
# 方法二： 删除单个固定位置的字符，可以使用切片 + 拼接的方式
# 方法三： 字符串的replace()方法或正则表达式re.sub()删除任意位置字符
# 方法四： 字符串translate()方法，可以同时删除多种不同字符
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# strip只能去掉开头和结尾的字符
# 使用切片的话，必须知道这个字符的固定位置
import re

s = 'abc:123'
print s[:3] + s[4:]

# replace()方法一次只能删除一种字符串
s2 = '\tabc\t123\txyz'
rs2 = s2.replace('\t', '')
print rs2

# sub()方法可以删除多种字符
s3 = '\tabc\t123\t\rxyz\ropq'
print re.sub('[\t\r]', '', s3)
