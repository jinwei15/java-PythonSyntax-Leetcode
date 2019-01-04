# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# Example 1:

# Input:  "69"
# Output: true
# Example 2:

# Input:  "88"
# Output: true
# Example 3:

# Input:  "962"
# Output: false

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) == 0: return True
        dic = {'1':'1', '0':'0', '6':'9', '8':'8','9':'6'}
        left = 0
        right = len(num) - 1
        
        while(left<=right):
            if dic.get(num[left]) != None and dic.get(num[right]) != None and dic[num[left]] == num[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
