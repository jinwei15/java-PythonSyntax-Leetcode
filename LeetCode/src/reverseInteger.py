# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         reversedNum = 0
#         input_long = x
#         flag = False
#         if input_long<0:
#             input_long = -input_long
#             flag = True

#         while (input_long != 0):
#             reversedNum = reversedNum*10 + input_long % 10
#             input_long = input_long//10
#         if reversedNum > (2**31) -1 :
#             return 0
#         else:
#             if flag == False:
#                 return reversedNum
#             else:
#                 return -reversedNum


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = -int(self.reverAny(-x))
        else:
            result = int(self.reverAny(x))
        
        if result > 2**31 -1 or result < -2**31 -1:
            return 0
        else:
            return result
        
    def reverAny(self,x):
        x = str(x)
        return x[::-1]
