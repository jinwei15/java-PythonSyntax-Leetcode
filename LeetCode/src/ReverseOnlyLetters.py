
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
    
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i, j = 0, len(S) - 1
        strList = list(S)
        while i < j:
            while i < j and not S[i].isalpha(): i += 1
            while i < j and not S[j].isalpha(): j -= 1
            strList[i] ,strList[j] = strList[j] ,strList[i]
            
            i += 1
            j -= 1
        return ''.join(strList)
