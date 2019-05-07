class Solution:
    def search(self, reader, target):
        #         """
        #         :type reader: ArrayReader
        #         :type target: int
        #         :rtype: int
        #         """
        #         left,right = 0,10000
        #         while(left<=right):
        #             mid = (left+right)//2
        #             if reader.get(mid) == target:
        #                 return mid
        #             elif reader.get(mid) == 2147483647 or reader.get(mid) > target:
        #                 right = mid - 1
        #             elif reader.get(mid) < target:
        #                 left = mid + 1
        #         return -1
        hi = 1
        while reader.get(hi) < target:
            hi = hi << 1
            print(hi)
        lo = hi >> 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if reader.get(mid) < target:
                lo = mid + 1
            elif reader.get(mid) > target:
                hi = mid - 1
            else:
                return mid
        return -1
