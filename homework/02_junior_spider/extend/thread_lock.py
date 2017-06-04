# coding: utf-8
# threading.Lock(): 得到锁对象，threading.acquire(): 加锁   threading.release(): 释放锁
import threading
import time

show_lock = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        time.sleep(1)
        with show_lock:
            print threading.current_thread().name, 'Hello world'

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

