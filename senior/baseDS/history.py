# coding: utf-8
# 2-7 如何实现用户的历史记录功能(最多n条)
"""
1、很多应用程序都有浏览用户的历史记录的功能，例如：
浏览器可以查看最近访问过的网页。
视频播放器可以查看最近播放过视频文件。
shell可以查看用户输入过的命令。
...
现在我们制作了一个简单的猜数字的小游戏，添加历史记录功能，
显示用户最近猜过的数字，如何实现？
"""
from random import randint
from collections import deque
import pickle

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 使用容量为n的队列存储历史记录，使用标准库collections中的deque，
# 它是一个双端循环队列。
# 程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print 'right'
        return True
    elif k < N:
        print '%s 小于这个数' % k
    else:
        print '%s 大于这个数' % k
    return False

while True:
    line = raw_input("请输入猜测的数字：")
    if line.isdigit():
        n = int(line)
        history.append(n)
        pickle.dump(history, open('histo', 'w'))
        if guess(n):
            break
    elif line == 'history' or line == 'h?':
        print list(history)

