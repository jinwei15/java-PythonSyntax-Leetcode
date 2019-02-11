#
#
# 4. closet two sum
#
# ..变种，选两部电影，电影时间总和小于飞行时间-30，
# 定义一个pair存index和time，按time排序，然后按two sum双指针就好了
#
#
# ..包裝貨物 TWO SUM 注意是要"剛好"的重量 具体的context是卡车装货物，两个货物的体积要求正好等于卡车体积减去30。如果有多个组合，选择有最大货物体积的那一组。
#
# ..飞机电影 2Sum Closest 给一个int[] 找到离target最近(<=)的两部电影的时间 return index
#
# ..飞机电影推荐
#
#           要求：从一系列电影中选取两部电影，这两部电影的播放时间刚刚好是飞行时间-30分钟。
#           建议先直接做 O(n*n) 方法，不然一开始会纠结 Failed Test Cases， 时间就没了。
#
# ... 飞机电影
# 给了飞行时间，一堆电影，找2个电影刚好可以在降落前30min看完，如果有多解，选包含最长电影的那个。2 sum 加一个如果出现多解的判断。
# Corner case是遍历所有电影后没有满足的解，需要返回空的list
# 一开始读错了题目，以为要找的是2 sum closest耽误了不少时间
#
#
# ..movie durarion  我是exact 30
#
# .. two sum closest truck题， 题目很简单 edge case要求有同样大的pair时选pair with largest pack 如 [110, 90] [190, 10] 时 选 [190, 10]  当时卡了十分钟的bug 仔细读完instruction才发现有这么个要求
#
# ..two sum变种，有一辆货车和一些货物，找到两个货物重量正好是货车capacity - 30，注意一下corner case，找不到的时候返回一个空list，但是题目中并没有提到。。。
#
# ..注意 飞机这个是exactly same 30不是之前说的小于等于 大家做面筋一定要好好读题 虽然别人的分享能帮我们提前准备但是自己要上心啊！！！
# 提供一下自己的最优解思路:
# 如果小于等于的条件用二分做
# 等于就two sum思路
#

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
    # 选两部电影，电影时间总和小于飞行时间 - 30，
    def twoSumCloest(self, durations, k):
        """

        :param durations: movie list,
        :param k:  integer flight time
        :return: [,]
        """

        if durations is None or len(durations) < 2:
            return [-1, -1]

        duration_list = []
        index = 0
        for duration in durations:
            duration_list.append((duration, index))
            index += 1
        duration_list.sort(key=lambda x: x[0])

        max_sum = -sys.maxsize - 1
        res = [-1, -1]
        start, end = 0, len(duration_list) - 1
        target = k - 30
        while start < end:
            start_d, start_idx = duration_list[start]
            end_d, end_idx = duration_list[end]
            curr_sum = start_d + end_d

            if curr_sum > target:
                end -= 1
            elif curr_sum > max_sum and curr_sum <= target:
                max_sum = curr_sum
                res[0] = min(start_idx, end_idx)
                res[1] = max(start_idx, end_idx)
                start += 1
            else:
                start += 1

        return res

    # two sum 题型 hashmap one pass 写法
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapList = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if mapList.get(complement) == None:
                mapList[nums[i]] = i
            else:
                return [mapList.get(complement), i]

        return None


bb = Solution()
bb.twoSumCloest()


