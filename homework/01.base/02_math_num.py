# ^_^ coding: utf-8
# 函数作业
"""
本案例主要考察判断、循环的思路，其中利用数字的规律，去完成判断完数和素数的检测函数
完数：这个数等于他本身所有的约数累加起来，那么这个数就是完数
素数：这个数除了被1和他本身整除外，都不能被他中间的其他数字整除的数，称为素数
"""


def ispfct_num(num):                    # 判断一个数字是否是完数
    if not isinstance(num, int):
        return False
    if num <= 3:
        return False
    divs = [1]
    sum_count = 1
    for i in range(2, num):
        if num % i == 0:
            divs.append(i)
            sum_count = sum_count + i

    if sum_count == num:
        return True
    else:
        return False


def isprimer_num(arg_num):              # 判断一个数字是否是素数
    if not isinstance(arg_num, int):
        return False
    if arg_num < 2:
        return False
    for i in range(2, arg_num):
        if arg_num % i == 0:
            return False
    return True


def check_pfct():
    snu = raw_input("please input number")
    try:
        nu = int(snu)
    except ValueError as err:
        print("input type error: {}".format(err))
        return False

    if ispfct_num(nu):
        print("the number:{} is perfect number".format(nu))
    else:
        print("the number:{} not perfect number".format(nu))


if __name__ == "__main__":
    arrPrimers = []
    arrPfcts = []
    for n in range(1, 200):
        if ispfct_num(n):
            arrPfcts.append(n)
        if isprimer_num(n):
            arrPrimers.append(n)

    print("1-200的素数有：")
    for pr in arrPrimers:
            print pr, ' ',

    print("\n1-200的完数有：")
    for pf in arrPfcts:
            print pf, ' ',
    print("")

    check_pfct()

