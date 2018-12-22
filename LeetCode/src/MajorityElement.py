# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


import collections

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       # # this is a python style! 
       # a = collections.Counter(nums)
       # return a.most_common(1)[0][0]
       #  this is a java style!
        b = dict()

        for i in nums :
            b[i] = b.get(i,0) + 1
        v=list(b.values())
        k=list(b.keys())
        return k[v.index(max(v))]
            
           










































































 
