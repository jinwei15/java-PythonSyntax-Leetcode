# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        subString = s
        l, r = 0, 0
        checkTable = {s[l]: l}
        if len(s) < len(t):
            return ''
        if len(s) == len(t) and self.allIn(t, s):
            return s
        elif len(s) == len(t) and not self.allIn(t, s):
            return ''

        while (l < len(s) and r <= len(s)):
            # print(l,r)
            if (self.allIn(t, s[l:r])):
                # print('yes in ')
                if len(s[l:r]) < len(subString):
                    subString = s[l:r]
                    # print(subString)
                found = False
                for i in range(l + 1, r):
                    if s[i] in set(t):
                        l = i
                        found = True
                        break
                if found == False:
                    return subString

            else:
                r += 1

        if self.allIn(t, s):
            return subString
        else:
            return ''

    # check if all the letters in the checkStr
    def allIn(self, target, checkStr):
        for char in target:
            if char not in checkStr:
                return False
        return True



bb = Solution()
# s = 'ADOBECODEBANC'
# t = 'ABC'
s = 'ab'
t = 'a'
res = bb.minWindow(s,t)
print(res)