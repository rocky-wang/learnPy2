# ^_^ coding: utf-8
# 4-4 如何将多个小字符串拼接成一个大的字符串
"""
1、在设计某网络程序时，我们自定义了一个基于UDP的网络协议，按照固定次序向服务器
传递一系列参数：
hwDetect:       "<0112>"
gxDepthBits:    "<32>"
gxResolution:   "<1024x768>"
fullAlpha:      "<1>"
loadDist:       "<100.0>"
DistCull:       "<500.0>"
在程序中我们将各个参数按次序收集到列表中：
["<0112>","<32>","<1024x768>","<60>","<1>","<100.0>","<500.0>"]
最终我们要把各个参数拼接成一个数据报进行发送。
"<0112><32><1024x768><60><1><100.0><500.0>"
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 方法一： 迭代列表，连续使用‘+’操作依次拼接每一个字符串。
# 方法二： 使用str.join()方法，更加快速的拼接列表中所有字符串
# --------------------------------------------------
# +号实际调用的是str类中的__add__方法，比较调用的是__gt__方法
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
pl = ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
s1 = ''

for p in pl:
    s1 += p

# 此方法存在巨大的浪费，因为每一次的结果都是一个临时的字符串，用后扔掉。
# 意味着大量的字符串拷贝和解释器的释放
print s1

# s.join(iterable)->string ，利用s作为分隔符，连接可迭代对象，返回成一个字符串
s2 = ';'.join(['abc', '123', 'xyz'])

print s2

# 也可以使用生成器表达式，这个比列表解析还要减少开销
s3 = ''.join([str(x) for x in pl])
print s3

