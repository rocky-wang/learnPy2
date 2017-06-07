# ^_^ coding: utf-8
# python的装饰器
# 原有函数的基础上，扩展这个函数的功能，不改变函数名称，利用闭包


# 装饰器(Decorator)，代码运行期间增加功能，但不改变原有功能的
def check(fn):
    def wrapper(a, b):
        print('check...')
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)
        print('variable cannot be add')
        return
    return wrapper


def my_add(a, b):
    return a + b

my_add = check(my_add)

print my_add(10, 20)


@check
def my_sub(a, b):
    return a * b

print my_sub(10, 20)


# 装饰器类
class Foo(object):
    def __init__(self, func):
        print('init...')
        self._func = func

    def __call__(self, a, b):
        print 'check...'
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return self._func(a, b)
        else:
            print('variable cannot be do this')


@Foo
def my_sub(a, b):
    return a - b

print my_sub(100, 20)

