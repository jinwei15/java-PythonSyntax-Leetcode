# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # below is a brute force method this will lead to time limit exceeded:
#         # this is very boring. need to think a smarter way.
#         length = len(height)
#         ans = 0
#         for i in range(1, length-1):
#             leftIndex = 0
#             rightIndex = 0
#             for j in range(i,-1,-1):
#                 leftIndex = max(leftIndex, height[j])
#             for j in range(i,length,1):
#                 rightIndex = max(rightIndex,height[j])
            
#             ans += min(leftIndex, rightIndex) - height[i]
        
#         return ans
                
                

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        ans = 0
        length = len(height)
        leftMax = [0 for i in range(length)]
        rightMax = [0 for i in range(length)]
        leftMax[0] = height[0]
        for i in range(1,length):
            leftMax[i] = max(height[i],leftMax[i-1])
        rightMax[length - 1] = height[length - 1]
        for i in range(length-2,-1,-1):
            rightMax[i] = max(height[i], rightMax[i+1])
        for i in range(1, length-1):
            ans += min(leftMax[i],rightMax[i]) - height[i]

        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
