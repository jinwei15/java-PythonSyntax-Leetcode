# 168. Excel Sheet Column Title

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# Example 1:

# Input: 1
# Output: "A"
# Example 2:

# Input: 28
# Output: "AB"
# Example 3:

# Input: 701
# Output: "ZY"

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = []

        d='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while(n != 0):
            reminder = (n - 1) % 26
            s.append(d[reminder])
            n = (n - 1)//26
        return ''.join(s[::-1])
        
       
            
        
        
