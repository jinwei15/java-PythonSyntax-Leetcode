class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        occr = dict()
        for i in nums:
            occr[i] = occr.get(i,0) + 1
        
        listNum = sorted(occr.items(), key=lambda x: x[1]，reverse = True)
        
        return listNum[0:k-1]
        
            
        
