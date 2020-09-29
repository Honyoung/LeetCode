#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from com.jensen.coding_fun import yield_keyword as ykw


def run():
    for i in ykw.yield_show(5):
        print('run:', i)