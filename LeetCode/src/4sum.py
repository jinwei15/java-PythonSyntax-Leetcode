# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# class Solution:
#     def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
#         nums.sort()
#         res = []
#         length = len(nums)
#         for i in range(length-2):
#             if i==0 or (i>0 and nums[i] != nums[i-1]):
#                 lo = i+1
#                 hi = length -1
#                 sum = 0- nums[i]
#                 while(lo<hi):
#                     if (nums[lo] + nums[hi] == sum):
#                         res.append([nums[i],nums[lo],nums[hi]])
#                         while(lo<hi and nums[lo]==nums[lo+1]):lo+=1
#                         while(lo<hi and nums[hi]==nums[hi-1]):hi-=1
#                         lo +=1
#                         hi -=1
#                     elif nums[lo] + nums[hi] < sum:
#                         lo += 1
#                     else:
#                         hi -= 1

#         return res


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
        return

