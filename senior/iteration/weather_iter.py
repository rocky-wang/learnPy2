# coding: utf-8
# 3-1 如何实现可迭代对象和迭代器对象(2)
"""
1、某软件要求，从网络抓取各个城市气温信息，并依次显示：
北京：15 ~ 20  天津：17 ~ 22  长春：12 ~ 18
如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，
并且浪费存储空间。我们期望以“用时访问”的策略，并且能把所有城市气温封装
到一个对象里，可以用for语句进行迭代，如何解决？
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 解决方案：
# 1、实现一个迭代器对象WeatherIterator，next方法每次返回一个城市气温
# 2、实现一个可迭代对象WeatherIterable，__iter__方法返回一个迭代器对象
# ----------------------------------------------------
# 这里使用第三方requests库，提供基本的http协议访问
# 因为回应数据是gzip压缩，该库可以自动解压缩，同时调用json()函数返回json对象
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import requests
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    @staticmethod
    def get_weather(city):
        url_info = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url_info)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        cit = self.cities[self.index].decode('utf-8')
        self.index += 1
        return self.get_weather(cit)

w1 = WeatherIterator(['北京', '成都', '济南'])

for w in w1:
    print w


class WeatherIteable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

print '_'*50
to1 = WeatherIteable(['重庆', '上海', '深圳'])

for x in to1:
    print x

