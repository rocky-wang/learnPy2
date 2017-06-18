# coding: utf-8


# 格式化打印字典信息
def dict_format_show(data):
    """
    根据字典中key值最长的进行格式化对齐输出
    :param data: 需要格式化显示输出的字典类型
    :return: None
    """
    if not isinstance(data, dict):
        print '[error]:DATA is not dict type!'
        return None
    keys_len = map(len, data.viewkeys())
    max_len = max(keys_len) + 1
    fo = "{k:<%d}: {v}" % max_len
    for y in data:
        print fo.format(k=y, v=data[y])

