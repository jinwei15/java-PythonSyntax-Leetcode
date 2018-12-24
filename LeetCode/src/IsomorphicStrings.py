# 205. Isomorphic Strings
# Easy


# Favorite

# Share
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.

# Accepted
# 174,692
# Submissions
# 483,524


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        table1 = dict()
        table2 = dict()
        for i in range(len(s)):
            if table1.get(s[i]) == None:
                table1[s[i]] = t[i]
            else:
                if table1[s[i]] != t[i]:
                    return False

            if table2.get(t[i]) == None:
                table2[t[i]] = s[i]
            else:
                if table2[t[i]] != s[i]:
                    return False
        return True

                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
