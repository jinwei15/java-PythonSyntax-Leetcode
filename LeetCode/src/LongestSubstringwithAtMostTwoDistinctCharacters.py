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
        if s == '': return 0
        
        # this is the initial sol lution is using a hashmap:
        
        longest = -sys.maxsize-1
        # longest = float('-inf')
        resultNum = 0
        
        checkTable = [0]*56
        
        n = len(s)
        for i in range(n):
            count = 0
            checkTable = [0]*56
            for j in range(i,n):
                if checkTable[ord(s[j]) - ord('a')] == 0:
                    count += 1
                    checkTable[ord(s[j]) - ord('a')] += 1
                if count <= 2:
                    resultNum += 1
                else:
                    break;
                if count <= 2 and j-i + 1 > longest:
                    longest = j-i+1
        return longest
                    
                    

                
        
