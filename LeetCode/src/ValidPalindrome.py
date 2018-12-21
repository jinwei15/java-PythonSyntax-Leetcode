# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
    
# we can use this math as well as reverse and compare

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower()
        # below is a two pointer method
        # left = 0
        # right = len(s)-1
        # while(left<=right):
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        # return True

        return s == s[::-1]
        
            
        
        
