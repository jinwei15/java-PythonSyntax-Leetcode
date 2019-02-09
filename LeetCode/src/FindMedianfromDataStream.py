# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.list = []

#     def addNum(self, num: 'int') -> 'None':

#         self.list.append(num)

#     def findMedian(self) -> 'float':
#         self.list.sort()

#         L = len(self.list)

#         if len(self.list) % 2 == 0:

#             return (self.list[(L//2)-1]  + self.list[(L//2)])*0.5


#         else:
#             return self.list[(L//2)]


from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHp = []
        self.maxHp = []

    def addNum(self, num: 'int') -> 'None':
        heappush(self.maxHp, -num)
        if len(self.maxHp) - len(self.minHp) == 2:
            temp = -heappop(self.maxHp)
            heappush(self.minHp, temp)
        if self.maxHp and self.minHp and - self.maxHp[0] > self.minHp[0]:
            temp = -heappop(self.maxHp)
            heappush(self.minHp, temp)

            temp2 = heappop(self.minHp)
            heappush(self.maxHp, -temp2)

    def findMedian(self) -> 'float':
        if len(self.maxHp) > len(self.minHp):
            return -self.maxHp[0]
        else:
            return (-self.maxHp[0] + self.minHp[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()