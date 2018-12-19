class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        countPair = dict()
        countResult = list()
        for item in cpdomains:
            elements = item.split(' ')
            countPair[elements[1]] = countPair.get(elements[1],0) + int(elements[0])
            while '.' in elements[1]:
                index = elements[1].find('.')
                elements[1] = elements[1][index+1:]
                countPair[elements[1]] = countPair.get(elements[1],0) + int(elements[0])
        #for key, value in countPair.items():
        #    item = str(value)+ ' '+ key  
        #    countResult.append(item)
        return ["{} {}".format(value, key) for key, value in countPair.items()]
            
    
