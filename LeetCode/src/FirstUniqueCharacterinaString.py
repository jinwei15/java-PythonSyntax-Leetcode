"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
import collections

def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    #         if len(s) == 0: return -1
    #         occu = dict()
    #         for i in s :
    #             occu[i] = occu.get(i,0) + 1

    #         ending = 0
    #         for index in range(len(s)):
    #             ending = index
    #             if occu[s[index]]==1:
    #                 return index

    #         if (ending == len(s)-1):
    #             return -1
    c = collections.Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
    return -1