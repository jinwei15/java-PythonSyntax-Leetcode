# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        result = ''
        if billion:
            result = self.getNum(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += self.getNum(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += self.getNum(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += self.getNum(rest)
        return result

    def getNum(self, num):
        table1 = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

        table3 = {
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }

        res = ''
        read = num // 100
        remain = num % 100

        if read > 0:
            res += table1.get(read, '') + ' ' + table3.get(100, '')

        if table1.get(remain) != None:
            res += ' ' if res else ''
            res += table1.get(remain)
        else:

            num -= read * 100
            read = num // 10
            remain = num % 10
            if read != 0 or remain != 0:
                res += ' ' if res else ''
                res += table1.get(read * 10, '') + ' ' + table1.get(remain, '')

        return res















