class Solution:
    #     def intToRoman(self, num: int) -> str:
    #         table = {
    #             1:'I',
    #             4:'IV',
    #             5:'V',
    #             9:'IX',
    #             10:'X',
    #             40:'XL',
    #             50:'L',
    #             90:'XC',
    #             100:'C',
    #             400:'CD',
    #             500:'D',
    #             900: 'CM',
    #             1000:'M'
    #         }

    #         numArr = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

    #         res = ''
    #         while(num>0):
    #             biggest = numArr[-1]
    #             quotient = num // biggest
    #             reminder = num % biggest
    #             numArr.pop()
    #             if quotient != 0:
    #                 res +=  quotient * table.get(biggest)
    #                 num -= quotient*biggest
    #         return res

    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i, v in enumerate(values):
            res += (num // v) * numerals[i]
            num %= v
        return res