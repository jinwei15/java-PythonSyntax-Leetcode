# import collection
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = collections.Counter(nums)
        return a.most_common(1)[0][0]

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:

#         dic = dict()
#         for i in nums:
#             if dic.get(i) != None:
#                 return i
#             else:
#                 dic[i] = dic.get(i,0) + 1
#         return -1
