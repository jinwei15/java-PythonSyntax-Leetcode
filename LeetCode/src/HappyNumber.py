class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {n}

        while(n!=1):
            sumNum = 0
            for ch in str(n):
                sumNum = sumNum + int(ch)**2
            if sumNum in seen:
                return False
            else:
                seen.add(sumNum)
                n = sumNum
        return True
            



