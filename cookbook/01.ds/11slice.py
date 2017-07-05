# ^_^ coding: utf-8
# 为分组命名，方便以后程序调试和阅读

ada1 = 'abcde032aebewq19.50adfad'


print ada1[5:8]
print ada1[14:19]

SEQ_SE = slice(5, 8, 1)
BMI_SE = slice(14, 19)

print ada1[SEQ_SE]
