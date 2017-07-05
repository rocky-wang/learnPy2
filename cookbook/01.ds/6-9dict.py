# ^_^ coding: utf-8
# 从collection中设置键的默认值为列表，可以达到1键多值的效果
# orderdic保证了字典加入的顺序
# 字典的值运算时，可以使用zip函数进行重构顺序，zip函数返回一个列表，里面保存了元组内容，他只能返回一次迭代


from collections import defaultdict, OrderedDict

m1_dict = defaultdict(lambda: 30)
m2_dict = defaultdict(list)

print m1_dict['ab']

m2_dict['a'].append(12)
m2_dict['a'].append(13)
m2_dict['a'].append(14)

print m2_dict['a']

a1 = {'z', 'w'}
print a1
