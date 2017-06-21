# ^_^ coding: utf-8
import hashlib


# 得到字符串的MD5值
def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()


