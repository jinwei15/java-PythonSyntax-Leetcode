import sys


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0: return 0
        if x == 1 or x == 2: return 1
        left = 0
        right = x
        while (True):
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid == x or (mid + 1) * (mid + 1) > x:
                return mid
            else:
                left = mid + 1

# public int sqrt(int x) {
#     if (x == 0)
#         return 0;
#     int left = 1, right = Integer.MAX_VALUE;
#     while (true) {
#         int mid = left + (right - left)/2;
#         if (mid > x/mid) {
#             right = mid - 1;
#         } else {
#             if (mid + 1 > x/(mid + 1))
#                 return mid;
#             left = mid + 1;
#         }
#     }
# }