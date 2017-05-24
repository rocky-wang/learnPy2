# ^_^ coding: utf-8
# 2-2 如何为元组中的每个元素命名，提高程序可读性？
"""
学生信息系统中数据为固定格式：
(名字,年龄,性别,邮箱地址,...)
学生数量很大为了减少存储开销，对每个学生信息用元组表示：
('Jim',16,'male','jim8721@gmail.com')
('LiLei',17,'male','leile@qq.com')
('Lucy',16,'female','lucy123@yahoo.com')
...
访问时，我们使用索引访问，大量使用索引降低程序的可读性，
如何解决这个问题？
"""
from collections import namedtuple

student1 = ('Jim', 16, 'male', 'jim8721@gmail.com')

# print student[0]
# if student[1] >= 18:
#     pass

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 方案1： 定义类似与其他语言的枚举类型，也就是定义一系列数值常量
# 方案2： 使用标准库中collections.namedtuple替代内置tuple
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

NAME, AGE, SEX, EMAIL = xrange(4)

print student1[NAME]

name_stu = namedtuple('nstu', ['name', 'age', 'sex', 'email'])
o1 = name_stu('Jim', 16, 'male', 'jim8721@gmail.com')

o2 = name_stu(name="LiLei", age=18, sex="male", email="leile@qq.com")

print o1.name
print o2.name

d1 = o1._asdict()

print d1
