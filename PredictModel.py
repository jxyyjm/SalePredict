__author__ = 'yujianmin'
# -*- coding:utf-8 -*-
# here try to build an model to predict the sale account #
class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __del__(self):
        pass
    def say(self):
        print(self.a)
        print(self.b)
    def Predict(self):
        pass
if __name__ == "__main__":
    CA = A(3, 4)
    CA.say()