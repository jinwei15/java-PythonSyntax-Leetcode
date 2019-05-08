class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while(left<right):
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return None
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         mapList = dict()
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if mapList.get(complement) == None:
#                 mapList[nums[i]] = i
#             else:
#                 return [mapList.get(complement) + 1, i + 1]
#
#         return None
