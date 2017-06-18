# coding: utf-8
# 给定一个字符串，去掉重复出现的字符，并按顺序输出

a = "aAsmr3idd4bgs7Dlsf9eAf"

a_list = list(a)

set_list = list(set(a_list))

set_list.sort(key=a_list.index)

print ''.join(set_list)
