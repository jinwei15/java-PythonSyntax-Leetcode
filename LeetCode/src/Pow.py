#######################  TLE  ########################
#
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             x = 1/x
#             n = -n
#         if n >= 0:
#             res = 1
#             for i in range(n):
#                 res = res*x
#             return res
#
########################  TLE  ##########################
     

########################  Resurrsive  ########################        
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             x = 1/x
#             n = -n
            
#         def fastPow(x,n):
#             if n == 0:
#                 return 1.0
#             half = fastPow(x,n//2)
#             if (n%2==0):
#                 return half*half
#             else:
#                 return half*half*x
            
#         return fastPow(x,n)
#######################  Resurrsive  ########################       

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        while(n>0):
            if n % 2 == 1:
                ans = ans * x
            x = x*x
                
            n = n // 2
        return ans
            
        
        
