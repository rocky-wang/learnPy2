# coding: utf-8
import random
MAX_NUM = 100
MIN_NUM = 1


def get_num_from_keyboard():
    str_res = raw_input("请输入猜测的数字：")
    try:
        res = int(str_res)
    except ValueError:
        print("你输入的是无效数字，浪费一次机会了")
        return -1
    return res


def show_result_to_screen(num, flags, count=-1):
    global MAX_NUM
    global MIN_NUM
    if flags > 0:                       # 数字猜的大了，提示用户输入范围
        print("猜的结果偏大，提示数字范围{} - {}".format(MIN_NUM, num))
        MAX_NUM = num
    elif flags < 0:                     # 数字猜的小了，提示用户输入范围
        print("猜的结果偏小，提示数字范围{} - {}".format(num, MAX_NUM))
        MIN_NUM = num
    else:                               # 猜正确了
        print("猜的结果正确，结果是{}".format(num))

    if count > 0:
        print("剩余次数：{}".format(count))
    else:
        print("继续猜吧")


def guess_start(res_num, input_handler=get_num_from_keyboard,
                output_handler=show_result_to_screen):
    guess_res = []
    max_count = 8

    for count in range(max_count):
        num = input_handler()
        guess_res.append(num)
        reside_num = max_count - count - 1
        if num < res_num:
            output_handler(num, -1, reside_num)
        elif num > res_num:
            output_handler(num, 1, reside_num)
        else:
            output_handler(num, 0, reside_num)
            return True
    return False


def get_random_num():
    return random.randint(MIN_NUM, MAX_NUM)

if __name__ == "__main__":
    result = get_random_num()
    print(result)
    guess_start(result)

