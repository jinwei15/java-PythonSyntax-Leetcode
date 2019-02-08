# from heapq import *
# class Solution:
#     def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
#         h = []

#         for i in points:
#             dis = i[0]**2 + i[1]**2
#             heappush(h,(dis,i))
#         res = []
#         for i in range(K):
#             res.append(heappop(h)[1])
#         return res


# from heapq import heappush, heappop, heappushpop

# class Solution:
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         kClosestPointsToOrigin = []

#         # add first k points
#         for i in range(K):
#             heappush(kClosestPointsToOrigin, (-(points[i][0]**2+points[i][1]**2), points[i]))

#         # maintain k closest in heap for the remaining points
#         for i in range(K, len(points)):
#             heappushpop(kClosestPointsToOrigin, (-(points[i][0]**2+points[i][1]**2), points[i]))

#         # return each point in the heap
#         return [heappop(kClosestPointsToOrigin)[1] for _ in range(K)]


# #     @staticmethod
# #     def getDistanceFromOrigin(point):
# #         return math.sqrt(point[0]**2 + point[1]**2)


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        # return each point in the heap
        return points[:K]



