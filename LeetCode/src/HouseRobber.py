class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        
        totals = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                totals[i] = nums[0]
            elif i == 1:
                totals[i] = max(totals[0], nums[i])
            else:
                totals[i] = max(totals[i-1], totals[i-2] + nums[i])
                
                
        return totals[-1]
