# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:

# Input: [1,2,3]
# Output: 6
# Example 2:

# Input: [1,2,3,4]
# Output: 24
# Note:

# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

# #first sol
# class Solution:
#     def maximumProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    
    
    
#we can also find the min1 min2 max1 and max1 max2 max 3 and compare
import sys
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min2 = sys.maxsize
        max1 = max2 = max3 = -sys.maxsize - 1
        for n in nums:
            if n <= min1:  # n is smaller than min1 and min2
                min2 = min1
                min1 = n
            elif n <= min2: # n is between min1 and min2
                min2 = n
                
            if n>= max1 :  # n is greater than all max1 max2 max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n>= max2: # n is between max1 and max2
                max3 = max2
                max2 = n
            elif n>= max3: # n is between max2 and max3
                max3 = n
        
        
        return max(min1*min2*max1, max1*max2*max3)
                

word = 'hot'
i = 1
d = {}
        
s = word[:i] + "_" + word[i+1:]
d[s] = d.get(s, []) + [word]

print(d)
print(s)

print(['hot'] + ['hot'])