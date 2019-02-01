# this is the file for the vaild parentheses

# we can use lsit as a stack

# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if len(s) % 2 != 0:
#             return False
#         addList = ['(','[','{']
#         popList = [')',']','}']
#         stack = list()
#         for ch in s:
#             if ch in addList:
#                 stack.append(ch)
#             else:
#                 if(len(stack) == 0 or not self.matches(stack.pop(),ch)):
#                     return False


#         return not stack

#     def matches(self,a,b):

#         if a == '(' and b ==')':
#             return True
#         elif a == '[' and b == ']':
#             return True
#         elif a == '{' and b=='}':
#             return True
#         else:
#             return False


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}
        stack = list()
        for ch in s:
            #ch is a closing bracket
            if ch in mapping:
                
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '±'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[ch] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(ch)
    
                    
        return not stack
