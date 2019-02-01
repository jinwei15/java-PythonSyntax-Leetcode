class WhoIsTheClosest:
    # list of indexes
    def closet(self, s, indexes):
        # character : [index1, index2]
        Map = dict()
        indexDis = [None for _ in range(len(s))]
        for i in range(len(s)):

            if Map.get(s[i]) == None:
                Map[s[i]] = [i]
                indexDis[i] = -1
            else:
                Map.get(s[i]).append(i)
                indexList = Map.get(s[i])
                print(indexList)

                lastIndex = len(indexList) - 1
                if lastIndex == 1:
                    indexDis[indexList[lastIndex-1]] = indexList[lastIndex]
                    indexDis[indexList[lastIndex]] = indexList[lastIndex - 1]
                elif lastIndex >= 2:
                    diffAfter = indexList[lastIndex] - indexList[lastIndex-1]
                    diffAhead = indexList[lastIndex-1] - indexList[lastIndex-2]

                    if diffAfter>diffAhead:
                        indexDis[indexList[lastIndex - 1]] = indexList[lastIndex]

                    indexDis[i] = indexList[lastIndex - 1]

        for i in indexes:
            print(indexDis[i])
        print(indexDis)


        # res = []
        # for index in indexes:
        #     ch_list = Map.get(s[index])
        #     if ch_list == None:
        #         res.append(-1)
        #     else:
        #         result = min(ch_list)

a = WhoIsTheClosest()
a.closet('hackerrank',[4,1,6,8])

# a.closet('babab',[2])

# test case 1:
#
# string: 'babab'
# index = [2]
# 0
#
# test case 2:
# string: 'hackerrank'
# index  = [4, 1, 6, 8]
#  -1 7 5 -1
