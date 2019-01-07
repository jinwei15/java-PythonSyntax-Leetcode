
# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1

# the below sol is wrong it is not in bigO (n) because i not in it is O(n^2) complexity so fucked up
class Solution:
    def firstMissingPositive(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        if nums == []: return 1
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
        # this is a very ugly solution how to solve it in bigO(n) is ver tough
        
        
