# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:

# Input: "aba"
# Output: True
# Example 2:

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:

# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

        
