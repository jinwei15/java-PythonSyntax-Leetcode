ven N, calculate F(N).

 

# Example 1:

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 0
        F = [0 for i in range(N+1)]
        F[0] = 0
        F[1] = 1
        for i in range(2,N+1):
            F[i] = F[i-1] + F[i-2]
        
        return F[N]
        
