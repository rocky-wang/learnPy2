# ^_^ coding: utf-8
# itemgetter：主要使用字典排序，查找最大最小值时，比较适用
# attrgetter：主要用于对象属性的获取
from operator import itemgetter
from operator import attrgetter

teamitems = [{'team': 'France', 'P': 1, 'GD': -3, 'GS': 1, 'GA': 4},
             {'team': 'Uruguay', 'P': 7, 'GD': 4, 'GS': 4, 'GA': 0},
             {'team': 'SouthAfrica', 'P': 4, 'GD': -2, 'GS': 3, 'GA': 5},
             {'team': 'Mexico', 'P': 4, 'GD': 1, 'GS': 3, 'GA': 2}
             ]

sorted(teamitems, key=itemgetter('P', 'GD', 'GS', 'GA'))
# sorted(teamitems, key=attrgetter('P', 'GD', 'GS', 'GA'))

print teamitems



