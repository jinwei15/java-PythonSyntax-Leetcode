class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        times = 0
        while 0 in nums: 
            nums.remove(0)
            times += 1
        
        for i in range(times):
            nums.append(0)


