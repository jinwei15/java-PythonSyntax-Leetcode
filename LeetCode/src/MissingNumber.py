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
        for number in range(len(nums) + 1):
            if number not in num_set:
                return number