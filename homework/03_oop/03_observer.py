# ^_^ coding: utf-8
# 观察者模式
# 一个事情(订阅者)发生后，通知所有注册到这个通知的人(观察者)


# 先定义一个抽象的主题类，当主题发生变化后，通知所有订阅主题的观察者
class Subject(object):
    # 注册观察者
    def register_observer(self, ob):
        pass

    # 删除观察者
    def remove_observer(self, ob):
        pass

    # 通知中心
    def notify_observers(self):
        pass


# 定义一个抽象观察类
class Observer(object):
    # 每个观察者都应该预留一个接收订阅者发送通知的接口
    def update(self, n):
        pass

#################################
#       具体实现
#################################


# 出版社类，典型的发布者，只有一个人，但是会有很多人订阅
class Publish(Subject):
    def __init__(self):
        super(Publish, self).__init__()
        self.observer = []
        self.__book_name = ''

    def register_observer(self, ob):
        if ob not in self.observer:
            self.observer.append(ob)

    def remove_observer(self, ob):
        if ob not in self.observer:
            self.observer.remove(ob)

    def notify_observers(self):
        for o in self.observer:
            o.update(self.__book_name)

    # 出版社开始进行数据更新了
    def pub_book(self, n):
        self.__book_name = n
        self.notify_observers()


# 学生，算是一个订阅者，应该有接收的接口即可
class PrimayStudent(Observer):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Primay Student name %(name)s, the age is %(age)s" % {"name": self.name, "age": self.age}

    def update(self, book_name):
        print self, "recv ", book_name


# 定义一个学校订阅者
class School(Observer):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "School name %(name)s " % {"name": self.name}

    def update(self, book_name):
        print self, "recv ", book_name

if __name__ == "__main__":
    pub = Publish()
    a1 = PrimayStudent('Jim', 8)
    a2 = PrimayStudent('Green', 7)
    s1 = School('哈佛大学')

    pub.register_observer(a1)
    pub.register_observer(a2)
    pub.register_observer(s1)

    pub.pub_book('如何学习python')
    pub.pub_book('鬼吹灯')
