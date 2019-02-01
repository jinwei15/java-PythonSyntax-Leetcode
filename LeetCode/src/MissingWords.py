class MissingWords:
    def missing(self, a, b):
        aList = a.split()
        bList = b.split()

        res = []

        aptr = bptr = 0

        while(bptr < len(bList)):
            b_temp = bList[bptr]
            while aptr < len(aList):
                a_temp = aList[aptr]
                if a_temp == b_temp:
                    aptr += 1
                    bptr += 1
                    break
                else:
                    res.append(a_temp)
                    aptr+=1
        while aptr < len(aList):
            res.append(aList[aptr])
            aptr += 1

        return res

a = MissingWords()
str1 = 'I am using HackerRank to improve programming'
str2 = 'am HackerRank to improve'

for str in a.missing(str1,str2):
    print(str)
