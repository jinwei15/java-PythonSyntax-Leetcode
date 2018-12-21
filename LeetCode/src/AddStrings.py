# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# return str(int(num1) + int(num2)) will vailte the rules but works

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
            
        return str(self.atoi(num1)+self.atoi(num2))
    
    def atoi(self,s):
        rtr=0
        for c in s:
            rtr=rtr*10 + ord(c) - ord('0')

        return rtr
    
    
