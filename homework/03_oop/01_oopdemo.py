# ^_^ coding: utf-8
from types import MethodType


# Py2和Py3类的构建方法不一致，同时__var这种形式，会被自动转换，欺骗为私有成员变量了
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

a1 = Student('Rocky', 90)

print dir(a1)
a1._Student__score = 100

print a1.get_score()
print type(a1)
print type(Student)


# 动态添加属性，方法给实例对象
class Animal(object):
    pass

c1 = Animal()
c1.name = '机器猫'


def greeting(self):
    print '我是 ', self.name

c1.greet = MethodType(greeting, c1)

c1.greet()

