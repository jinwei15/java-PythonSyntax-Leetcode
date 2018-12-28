# Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
#
# Return the difference between the sum of the two integers and the target.
#
#
#
# Example
# Given array nums = [-1, 2, 1, -4], and target = 4.
#
# The minimum difference is 1. (4 - (2 + 1) = 1).
#
#
#
# Challenge
# Do it in O(nlogn) time complexity.
#
#
#
# 思路
# 这个套路的题就是先排序。
# 排完从两边往当中走。
# 当我们发现sum < target，说明要再大一点会更接近target。那么往右走。
# 反之当sum > target，说明要再小一点会更接近target。那么往左走。

import sys
class Solution:
    def twoSumClose(self, arr, target):
        """

        :param arr: arr:list,
        :param target:  target: integer
        :return: difference between the sum of the two integers and the target.
        """
        a = 0

    def twoSumCloest(self, durations, k):

        if durations is None or len(durations) < 2:
            return [-1, -1]

        duration_list = []
        for duration in durations:
            duration_list.append((duration, index))
        duration_list.sort()

        max_sum = -sys.maxsize
        res = [-1, -1]
        start, end = 0, len(duration_list) - 1
        target = k - 30
        while start < end:
            start_d, start_idx = duration_list[start]
            end_d, end_idx = duration_list[end]
            curr_sum = start_d + end_d

            if curr_sum > target:
                end -= 1
            elif curr_sum > max_sum:
                max_sum = curr_sum
                res[0] = min(start_idx, end_idx)
                res[1] = max(start_idx, end_idx)
                start += 1
            else:
                start += 1

        return res


