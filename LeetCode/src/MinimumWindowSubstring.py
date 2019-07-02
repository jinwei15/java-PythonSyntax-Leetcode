# # Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# # For example,
# # S = "ADOBECODEBANC"
# # T = "ABC"
# # Minimum window is "BANC".
import collections
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present
        # in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C.
        # Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = dict()

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# import collections
# class Solution:

#     def minWindow(self, s: str, t: str) -> str:
#         subString = s
#         l, r = 0, len(t) - 1

#         if len(s) < len(t):
#             return ''
#         if len(s) == len(t) and self.allIn(t, s):
#             return s
#         elif len(s) == len(t) and not self.allIn(t, s):
#             return ''

#         while (l < len(s) and r <= len(s)):
#             # print(l,r)
#             if (self.allIn(t, s[l:r])):
#                 # print('yes in ')
#                 if len(s[l:r]) < len(subString):
#                     subString = s[l:r]
#                     # print(subString)
#                 found = False
#                 for i in range(l + 1, r):
#                     if s[i] in set(t):
#                         l = i
#                         found = True
#                         break
#                 if found == False:
#                     return subString

#             else:
#                 r += 1

#         if self.allIn(t, s):
#             return subString
#         else:
#             return ''

#     # check if all the letters in the checkStr
#     def allIn(self, target, checkStr):
#         counter = collections.Counter(checkStr)
#         for char in target:
#             if counter.get(char) == None or counter.get(char) == 0:
#                 return False
#             else:
#                 counter[char] = counter.get(char) - 1

#         return True






bb = Solution()
# s = 'ADOBECODEBANC'
# t = 'ABC'

s = 'ab'
t = 'a'

# s = 'a'
# t = 'ab'

# s = 'a'
# t = 'a'

# s = "bbaa"
# t = "aba"
res = bb.minWindow(s,t)
print(res)