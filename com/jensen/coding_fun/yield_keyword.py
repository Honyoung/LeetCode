#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
python yield 关键字 功能实现

yield 的作用就是把一个函数变成一个 generator
执行到yield语句时，就返回，然后从下一条语句继续执行
"""


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 相当于声明b为iterable类型返回
        a, b = b, a + b
        n = n + 1


def yield_show(n):
    print('hello')
    for i in range(n):
        print('---yield before----', i)
        yield i*i
        print('-------------i*i-------------', i*i)
        yield  i*2
        print('i*2=', i*2)





