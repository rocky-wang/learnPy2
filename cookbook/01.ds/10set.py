# ^_^ coding: utf-8
# 删除重复元素，并保证依然按照顺序，如果只用set方法，不能保证顺序

a = [1, 5, 2, 1, 9, 1, 5, 10]

# b = set(a)

print a
# print b


def mydeque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item      # 若不加，则变为普通集合返回，仍然无序
            seen.add(item)

print list(mydeque(a))

