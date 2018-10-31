class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        occ = dict()
        longestNow = 0
        secondLong = 0
        for i in s:
            occ[i] = occ.get(i, 0) + 1

            if occ[i] > 1:
                if (secondLong < longestNow):
                    secondLong = longestNow
                longestNow = 1
                occ.clear()
                occ[i] = 1

            else:
                longestNow += 1

        if (secondLong < longestNow):
            return longestNow
        else:
            return secondLong

d = Solution()
print(d.lengthOfLongestSubstring("dvdf"))