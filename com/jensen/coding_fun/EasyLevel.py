# -*- coding: UTF-8 -*-
'''
    @author: jensen.liu
    @date: Nov 9, 2020
'''

import time
from functools import reduce
# from itertools import combinations_with_replacement


def log(method_name):
    print('执行方法{}。当前时间:'.format(method_name), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


class Solution:
    def __init__(self):
        self.current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @staticmethod
    def get_instance(self):
        return Solution()

    def two_sum(self, nums, target):
        """

        :param nums:list[int]
        :param target:int
        :return:list[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [i, lookup[target-num]]
            else:
                lookup[num] = i

    def three_sum(self, nums):
        """
        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.
        Notice that the solution set must not contain duplicate triplets.
        Example 1:
            Input: nums = [-1,0,1,2,-1,-4]
            Output: [[-1,-1,2],[-1,0,1]]

        :param nums:
        :return:
        """
        rs = []
        for i, num1 in enumerate(nums):
            _lookup = {}
            for j, num2 in enumerate(nums):
                if j == i:
                    continue
                if -num2-num1 in _lookup.values():
                    rs.append([num1, num2, -num2-num1])
                _lookup[j] = num2
        return rs

    def reverse_integer(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        Note:
        Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

        Example 1:
        Input: x = 123
        Output: 321

        Example 2:
        Input: x = -123
        Output: -321

        Example 3:
        Input: x = 120
        Output: 21

        Example 4:
        Input: x = 0
        Output: 0


        Constraints:

        -231 <= x <= 231 - 1

        :param x: int
        :return: int
        """

        return


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1, 3, -4, 0, -1]
    target = 6
    print('nums:{},target:{}'.format(nums, target))
    print(solution.three_sum(nums))
