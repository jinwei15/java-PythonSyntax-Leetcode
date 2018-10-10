class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        centre = 0
        pair = 0
        alphabet = dict()

        #loop each character in s
        for ch in s:
            alphabet [ch] = alphabet.get(ch,0)+1
        if len(alphabet) == 1:
            return len(s)
        for key,value in alphabet.items():
            if value % 2 ==0 :
                pair = pair + value
            elif value % 2 > 0:
                pair = pair + (value - 1)
                centre = 1

        return pair+centre
