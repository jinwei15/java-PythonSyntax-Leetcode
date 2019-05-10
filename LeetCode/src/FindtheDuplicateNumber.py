# # import collection
# class Solution:
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         a = collections.Counter(nums)
#         return a.most_common(1)[0][0]

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:

#         dic = dict()
#         for i in nums:
#             if dic.get(i) != None:
#                 return i
#             else:
#                 dic[i] = dic.get(i,0) + 1
#         return -1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if (len(nums) > 1):
            slow = nums[0]
            fast = nums[0]
            while (fast != None and slow != None):
                slow = nums[slow]
                fast = nums[nums[fast]]
                if fast == slow: break
            print(slow)
            fast = nums[0]
            while (fast != slow):
                fast = nums[fast]
                slow = nums[slow]
            return slow
        return -1