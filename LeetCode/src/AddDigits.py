class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        for ch in str(num):
            sum = sum + int(ch)
        
        if sum<10:
            return sum
        else:
            return self.addDigits(sum)
