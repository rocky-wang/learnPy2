# coding: utf-8
# threading.current_thread() : 获取当前线程的ID号等信息
# threading.active_count() : 当前存活线程的数量
# threading.enumerate() : 当前存活线程的列表信息
import threading
import time


def greet_thhandler():
    print threading.current_thread()
    time.sleep(1)
    print 'hello world'

if __name__ == '__main1__':
    start = time.time()
    for x in xrange(5):
        greet_thhandler()

    end = time.time()
    print 'used time: ', end - start

if __name__ == '__main2__':
    start = time.time()
    thread_pool = []
    for x in xrange(5):
        t = threading.Thread(target=greet_thhandler)
        t.start()
        thread_pool.append(t)

    print threading.active_count()
    print threading.enumerate()
    for i in thread_pool:
        i.join()

    end = time.time()
    print 'used time: ', end - start


class MyThread(threading.Thread):
    def run(self):
        time.sleep(1)
        print threading.current_thread().name, 'my hello world'

if __name__ == '__main__':
    start = time.time()
    thread_pool = []
    for x in xrange(5):
        t = MyThread()
        t.start()
        thread_pool.append(t)

    for i in thread_pool:
        i.join()
    end = time.time()
    print 'used time: ', end - start
