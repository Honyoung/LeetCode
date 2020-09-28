#!/bin/usr/python3
from com.jensen.leetcode import CombineInteger as ci


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.b, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


if __name__ == '__main__':
    print('开始运行程序')

    # ci.run()
    for n in Fab(5):
        print(n)
