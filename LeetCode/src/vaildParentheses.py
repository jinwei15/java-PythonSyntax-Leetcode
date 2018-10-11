# this is the file for the vaild parentheses

# we can use lsit as a stack

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        addList = ['(','[','{']
        popList = [')',']','}']
        stack = list()
        for ch in s:
            if ch in addList:
                stack.append(ch)
            else:
                if(len(stack) == 0 or not self.matches(stack.pop(),ch)):
                    return False


        return not stack

    def matches(self,a,b):

        if a == '(' and b ==')':
            return True
        elif a == '[' and b == ']':
            return True
        elif a == '{' and b=='}':
            return True
        else:
            return False
