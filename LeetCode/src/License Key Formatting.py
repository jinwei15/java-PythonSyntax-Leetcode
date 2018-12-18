class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # remove all the dashes
        
        # calculate how many dashes we need to insert 
        
        # insert the dashes == reminder + number_n * K_length elements 
        
        S = S.replace('-','').upper()
        number_n = len(S)//K
        reminder = len(S) - number_n * K
        
        #insert from the end of tbe string
        position = len(S)
        for i in range (number_n):
            position = position - K 
            if position > 0:
                S = S[:position] + '-' + S[position:]
        
        return S
