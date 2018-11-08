class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        reList = dict()
        reList2 = dict()
        indexMin = float('inf')
        resultList = []
        for i in range(len(list1)):
            reList[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in reList: # and i+reList.get(list2[i]) < indexMin:
                reList2[list2[i]] = reList.get(list2[i]) + i 
                # resultList.append(list2[i])
        result = sorted(reList2.items(), key=lambda x: x[1])
        print(result)
        for item in result:
            if item[1] <= indexMin:
                indexMin = item[1]
                resultList.append(item[0])
                
        return resultList
        
