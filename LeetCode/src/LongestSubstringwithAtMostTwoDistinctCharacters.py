import sys


# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.






# https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        
        
        """
#         if s == '': return 0
        
#         # this is the initial sol lution is using a hashmap:
        
#         longest = -sys.maxsize-1
#         # longest = float('-inf')
#         resultNum = 0
        
#         checkTable = [0]*56
        
#         n = len(s)
#         for i in range(n):
#             count = 0
#             checkTable = [0]*56
#             for j in range(i,n):
#                 if checkTable[ord(s[j]) - ord('a')] == 0:
#                     count += 1
#                     checkTable[ord(s[j]) - ord('a')] += 1
#                 if count <= 2:
#                     resultNum += 1
#                 else:
#                     break;
#                 if count <= 2 and j-i + 1 > longest:
#                     longest = j-i+1
#         return longest


       # Initialize sliding window and counts of chars in the window
        # Worst case time and space complexity:
        # Time: O(N), Space: O(W) where N is size of string and W is size of max window
        
        left = 0
        right = 0
        counts = dict()
        maxlength = 0
        # Slide the window down the string until we reach the end
        #
        # Loop invariant:
        # (1) The previously seen window is s[left:right]
        # (2) The right index - left index of window is always the length
        #     of the longest substring with <= 2 distinct characters
        while right < len(s):
            # Slide the right end up and update counts such that the window is now s[left:right+1]
            counts[s[right]] = counts.get(s[right],0) + 1
            right += 1
            
            # If the window has more than 2 characters, slide the left end of 
            # the window up and update counts such that the window is now s[left+1:right+1]
            if len(counts) > 2:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            # print(right - left, " sep", left, right)
        # The length of the window is the length of the longest valid substring
        return right - left
                    
                    

                
        
