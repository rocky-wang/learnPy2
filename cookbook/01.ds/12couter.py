# ^_^ coding: utf-8
# 统计功能
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_cout = Counter(words)

print word_cout.most_common(3)
print word_cout['into']

da1 = '中国'
print da1[0:3]

