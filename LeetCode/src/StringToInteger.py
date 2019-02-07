# mplement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, s: 'str') -> 'int':
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        ls = list(s.strip())
        if len(ls) == 0: return 0
        if len(s) == 0: return 0

        if ls[0] == '-':
            sign = -1
        else:
            sign = 1

        if ls[0] in {'-', '+'}: del ls[0]

        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            # ret = ret*10 + int(ls[i])
            i += 1

        if sign * ret > 2 ** 31 - 1:
            return 2 ** 31 - 1

        elif sign * ret < -2 ** 31:
            return -2 ** 31

        return sign * ret

        # return max(-2**31, min(sign * ret, 2**31-1))

