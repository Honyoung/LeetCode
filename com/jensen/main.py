#!/bin/usr/python3
# -*- coding: UTF-8 -*-
import numpy as np

from com.jensen.leetcode import combine_integer as ci
from com.jensen.coding_fun import coding_fun as cf

if __name__ == '__main__':
    print('开始运行程序')

    # cf.run()
    list1 = np.arange(1,6)
    # print(list1)
    # print(tuple(list1))
    pool = tuple(list1)
    indices = list(range(2))
    print(tuple(pool[i] for i in indices))
    print(list(reversed(range(5))))
