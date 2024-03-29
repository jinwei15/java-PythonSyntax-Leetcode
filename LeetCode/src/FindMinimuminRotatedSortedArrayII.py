# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# #
# # (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# #
# # Find the minimum element.
# #
# # The array may contain duplicates.
# #
# # Example 1:
# #
# # Input: [1,3,5]
# # Output: 1
# # Example 2:
# #
# # Input: [2,2,2,0,1]
# # Output: 0
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while (left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                if nums[mid] == nums[left]:
                    left += 1
                    right -= 1
                else:
                    right = mid

        return nums[right]