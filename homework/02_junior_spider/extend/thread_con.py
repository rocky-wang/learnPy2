# ^_^ coding: utf-8
# 利用condition完成线程的同步
import threading

buf_condition = threading.Condition()
data = []


class StatisisLen(threading.Thread):
    def __init__(self, buf, con):
        super(StatisisLen, self).__init__()
        self.data = buf
        self.cond = con

    def run(self):
        for _ in xrange(5):
            self.cond.acquire()
            print threading.current_thread().name, '开始统计字符长度'
            if len(self.data) == 0:
                print threading.current_thread().name, '没有数据'
                self.cond.wait()
            print threading.current_thread().name, '统计开始...'
            while len(self.data) > 0:
                x = self.data.pop(0)
                print x, ' : ', len(x)
            self.cond.notify()
            self.cond.release()


class InputData(threading.Thread):
    def __init__(self, buf, con):
        super(InputData, self).__init__()
        self.data = buf
        self.cond = con

    def run(self):
        for _ in xrange(5):
            self.cond.acquire()
            if len(self.data) > 0:
                print threading.current_thread().name, '还有数据没有统计'
                self.cond.wait()
            print threading.current_thread().name, '可以输入数据了'

            while True:
                tbuf = raw_input('输入数据：')
                if tbuf[:5] == 'quit':
                    break
                self.data.append(tbuf)
            self.cond.notify()
            print threading.current_thread().name, '可以统计了哦'
            self.cond.release()

if __name__ == '__main__':
    th_count = StatisisLen(data, buf_condition)
    th_input = InputData(data, buf_condition)
    th_count.start()
    th_input.start()

    th_count.join()
    th_input.join()

