# ^_^ coding: utf-8
# 文件操作


def input_log_tofile(filename):
    while True:
        mes1 = raw_input("请输入文件内容，exit或者quit退出： ")
        if mes1 in ("exit", "quit"):
            with open(filename, "r") as fp1:
                for buf in fp1.readlines():
                    print buf.decode('gb2312'),
            break
        else:
            with open(filename, "a") as fp:
                fp.write(mes1.decode('utf-8').encode('gb2312') + "\n")
    return True

if __name__ == "__main__":
    input_log_tofile("input.log")
