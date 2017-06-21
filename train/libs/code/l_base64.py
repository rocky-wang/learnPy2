# ^_^ coding: utf-8
# 对每3个字节进行组合编码，3个字节共存24bit，这样分成4组，每组6bit
# 那么为什么要6bit那，因为a-zA-Z0-9再加上+/2个特殊字符，构成了26+26+10+2 = 64个状态
# 如果编码后的结果需要在URL中体现，那么就必须使用urlsafe_b64encode这类函数
import base64

str1 = 'abcd'

en_st1 = base64.b64encode(str1)

print en_st1


# 在传输过程中，自动补齐的=号
def safe_base64_decode(s):
    return base64.b64decode(s + '='*(len(s) % 4))

print safe_base64_decode('YWJjZA==')
print safe_base64_decode('YWJjZA')
