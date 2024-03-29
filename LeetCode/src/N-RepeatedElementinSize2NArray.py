# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

# Return the element repeated N times.

 

# Example 1:

# Input: [1,2,3,3]
# Output: 3
# Example 2:

# Input: [2,1,2,5,3,2]
# Output: 2
# Example 3:

# Input: [5,1,5,2,5,3,5,4]
# Output: 5


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A) / 2
        table = dict()
        for i in A:
            table[i] = table.get(i,0)+1
        
        for key,value in table.items():
            if value == N:
                val = key
        return val
                
        
            
            
#             this question is very tricky because the counter larger than 1 must be the answer.
        
