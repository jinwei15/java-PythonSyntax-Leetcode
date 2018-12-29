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

