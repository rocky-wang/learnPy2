# ^_^ coding: utf-8
# datetime是python处理时间和日期的特定格式标准库
# 他不同于字符串形式，内部可以对时间进行处理
from datetime import datetime, timedelta, tzinfo
import time

now = datetime.now()

print now

mydata1 = datetime(1995, 2, 19, 12, 18)

print mydata1.utctimetuple()

print datetime.fromtimestamp(1.0)

print datetime.fromtimestamp(time.time())
