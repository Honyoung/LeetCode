#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from com.jensen.coding_fun import yield_keyword as ykw
from com.jensen.coding_fun import generator_coding as gc
import numpy as np


def run():
    # for i in ykw.yield_show(5):
    #    print('run:', i)
    s = np.arange(1,5)
    print(list(gc.combinations(s, 2)))