# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ''
        # brute force search
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if i == j and len(longest) == 0:
                    longest = s[i]
                elif self.isPalindrome(s[i:j]) and len(s[i:j])>len(longest) :
                    longest = s[i:j]

        return longest
                
                
    def isPalindrome(self,letter):
        return letter == letter[::-1]
        
        
