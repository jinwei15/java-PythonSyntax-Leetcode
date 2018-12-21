# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
# all slicing window problems very useful
# 438. Find All Anagrams in a String
# Easy

# 1221

# 90

# Favorite

# Share
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# Accepted
# 94,870
# Submissions
# 268,450


#my first idea is that to remain a hashtable window and keep looping the the long string form 0 to len(long string) - len(short string)
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        block = dict()
        winBlock = dict()
        returnList = list()
        
        for ch in p:
            block[ch] = block.get(ch,0)+1
            
        for i in range(0,len(s)):
            
            if i-len(p)>=0:
                occur = winBlock.get(s[i-len(p)]) - 1
                if occur ==0:
                    del winBlock[s[i-len(p)]]
                else:
                    winBlock[s[i-len(p)]] = occur
                    
            winBlock[s[i]] = winBlock.get(s[i],0)+1
            # print(winBlock)
            # print(i+1-len(p))
            if winBlock == block:
                returnList.append(i+1-len(p))
        
        return returnList
                
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
