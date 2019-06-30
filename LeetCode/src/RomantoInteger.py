# class Solution:
#     def romanToInt(self, s: str) -> int:
#         table = {
#             'I':             1,
#             'V':             5,
#             'X':             10,
#             'L':             50,
#             'C':             100,
#             'D':             500,
#             'M':             1000
#         }
#         res = 0
#         i = 0
#         length = len(s)
#         while(i<length):
#             if s[i] == 'I' and i+1<length and (s[i+1] == 'V' or s[i+1] == 'X'):
#                 res += table.get(s[i+1]) - table.get(s[i])
#                 i += 2
#             elif s[i] == 'X' and i+1<length and (s[i+1] == 'L' or s[i+1] == 'C'):
#                 res += table.get(s[i+1]) - table.get(s[i])
#                 i += 2
#             elif s[i] == 'C' and i+1<length and (s[i+1] == 'D' or s[i+1] == 'M'):
#                 res += table.get(s[i+1]) - table.get(s[i])
#                 i += 2
#             else:
#                 res += table.get(s[i])
#                 i += 1
#         return res


class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]