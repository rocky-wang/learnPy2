# ^_^ coding: utf-8
# 1、解压序列赋值给多个变量
# 在python中元组、列表、可迭代对象(字符串、迭代器、生成器)，使用相应数量的变量作为接收，则自动解压序列赋值给对应对象
# 这里要注意，接收变量的数量必须和元素个数一致，不一致，可以使用_等变量作为占位符
# 利用*abc变量来指代任意多的元素，但是3.0以后才支持

name, age = ['rocky', 32]

print name
print age

