class Solution:

    def __init__(self):
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        self.resultlist = []

    def combine(self, combination, digits):
        if len(digits) == 0:
            self.resultlist.append(combination)

        else:
            for char in self.phone[digits[0]]:
                self.combine(combination + char, digits[1:])

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            self.combine('', digits)

        return self.resultlist