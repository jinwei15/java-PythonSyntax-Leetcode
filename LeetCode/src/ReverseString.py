class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s)-1
        while(left<right):
            s[left] , s[right] = s[right],s[left]
            left += 1
            right -= 1
            
        

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
        
#         def helper(s,start,end):
#             if start >= end:
#                 return

#             s[start],s[end] = s[end],s[start]
#             helper(s,start+1,end-1)
            
            
        
#         helper(s,0,len(s)-1)
        
        
            
        
        
        

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        
