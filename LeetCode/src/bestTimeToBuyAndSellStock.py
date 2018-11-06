class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minValue = float('inf')
        diff = 0
        for i in prices:
            if i < minValue:
                minValue = i
            temp = i - minValue
            if temp > diff:
                diff = temp
        return diff
                
        
