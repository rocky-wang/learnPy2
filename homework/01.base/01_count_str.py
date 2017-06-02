# ^_^ coding: utf-8
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：isalpha方法判断是否是字母，isspace方法判断是否是空格，isdigit方法判断是否是数字


# 统计特殊字符的次数函数statistic
def statistic_str(str_mes):
    result = {"letters": 0, "spaces": 0, "numbers": 0, "others": 0}
    for mes in str_mes:
        if mes.isdigit():
            result["numbers"] = result["numbers"] + 1
        elif mes.isspace():
            result["spaces"] = result["spaces"] + 1
        elif mes.isalpha():
            result["letters"] = result["letters"] + 1
        else:
            result["others"] = result["others"] + 1
    return result

if __name__ == "__main__":
    mes1 = raw_input("输入要统计的字符串：")
    res1 = statistic_str(mes1)
    stat_str_model = "统计结果: 英文字母数:{r[letters]}, " \
                     "空格数:{r[spaces]}, 数字数:{r[numbers]}, " \
                     "其他字符数:{r[others]}"
    print(stat_str_model.format(r=res1))

