# ^_^ coding: utf-8


# 给类函数添加构造方法
class Stu(object):
    pass


def set_score(self, var):
    self.score = var

Stu.myset = set_score

a1 = Stu()
a1.myadd = 200
a1.myset(10)

print a1.score
print a1.myadd


# slots这个是给实例变量添加属性的限制，对类属性添加不会有影响
# 对继承的子类没有作用
class Myslot(object):
    __slots__ = ('abc', 'foo')

Myslot.abc = 10
Myslot.fun = 20

a2 = Myslot()
print a2.fun
# a2.ds = 100


class Hiber(Myslot):
    pass

a3 = Hiber()
print a3.abc

a3.ds = 100


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

a1 = Student()
a1._score = 80
print a1._score

