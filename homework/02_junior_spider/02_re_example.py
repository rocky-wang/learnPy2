# coding: utf-8
# 正则表达式练习
# 匹配任意字符 .*     [\w\W]*     [\d\D]*     [\s\S]*
# 匹配邮箱  手机号
import re

tele_regex = re.compile('(?:13[0-9]|15[^4\D]|18[024-9])\d{8}')

str1 = '我的电话号码是：15565412879，另外一个号码13562318899.'

tele_lists = tele_regex.findall(str1)

print tele_lists

first = tele_regex.search(str1)

if first:
    print first.lastindex
    print first.group(0)

bak = re.sub(tele_regex, 'abc', str1)
print str1
print bak
