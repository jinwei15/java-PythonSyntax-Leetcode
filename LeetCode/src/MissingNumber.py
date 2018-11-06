class Solution:
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 return i
#             if i == len(nums)-1:
#                 return i+1
 
     def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
