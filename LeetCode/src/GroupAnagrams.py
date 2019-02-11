class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            # print(key)
            d[key] = d.get(key, []) + [w]
        return d.values()

# class Solution:
#     def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
#         ans = collections.defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             ans[count].append(s)
#         return ans.values()
