# 266. Palindrome Permutation
# Easy
# Share
# Given a string, determine if a permutation of the string could form a palindrome.
# Example 1:

# Input: "code"
# Output: false
# Example 2:

# Input: "aab"
# Output: true
# Example 3:

# Input: "carerac"
# Output: true

class Solution:
    def canPermutePalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # paralindome like aba using hashtable solution:
#         counter = dict()
#         countOdd = countEven = 0
#         for v in s:
#             counter[v] = counter.get(v,0)+1
        
#         for key,value in counter.items():
#             if value % 2 != 0 : countEven += 1 
        
#         return countEven<=1
    
        #paralindome using hashset solution:
        charSet = set()
        for ch in s:
            if ch in charSet:
                charSet.remove(ch)
            else:
                charSet.add(ch)
        return len(charSet) <= 1        
