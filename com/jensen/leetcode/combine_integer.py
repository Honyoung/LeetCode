#!/bin/usr/python3

from itertools import combinations
import numpy as np


def combine_integer():
    """

组合数

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
​
示例:
输入: n = 4, k = 2
输出:
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]

    """
    i = input("Input two integers n and k:")
    print(i)
    s = np.arange(1, int(i[0])+1)
    print(list(combinations(s, int(i[2]))))
    print('test')


def run():
    combine_integer()
