# 5. Find K nearest points
# ..返回距离原点最近的k个最近点－函数名ClosestXdestinations参考思路：for 每个点，算dist, heapify 所有点，最后pop k top points。时间:O(n+klogn)
# ..1.一堆蔬菜店（牛排店）的坐标，给了个原点（0，0），求k个距离最近的店， 等同于林扣六一二（缩水版 ，因为这道题oa题把原点坐标定死了反而操作少了些）
# ..1： 原题：求最近的几家牛排店，给一个有几个多标点的list和int k，求最近的k个牛排店。
#


# find k nearest point:
#  1) Given a list of points, and a point, find the K closest points and return
#  the list
#  658. Find K Closest Elements

import heapq
class Solution:

    def findClosestElements(self, alllocations, destination, k):
        """

        :param alllocations: [[1,2],[2,2],[8,9]]
        :param destination: [3,2]
        :param k:
        :return:
        """
        H = []
        heapq.heapify(H)
        for i in range(len(alllocations)):
            if i < k:
                heapq.heappush(H, alllocations[i])

