# coding: utf-8
from Tkinter import *


class App:
    def __init__(self, master):
        fra1 = Frame(master)
        fra1.pack()

        self.btn = Button(fra1, text='Hello Class', fg='red', command=fra1.quit)
        self.btn.pack()
        self.hibtn = Button(fra1, text='Say Hi', command=self.say_hi)
        self.hibtn.pack()

    @staticmethod
    def say_hi():
        print 'Hi rocky'

root = Tk()
app = App(root)
root.mainloop()
