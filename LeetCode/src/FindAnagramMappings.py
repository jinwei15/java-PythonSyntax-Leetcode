class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        aDict = dict()
        result = [0]*len(B)
        for j in range(len(B)):
            aDict[B[j]] = j

        for i in range(len(A)):
            print(aDict[A[j]])
            result[i] = aDict[A[i]]
        return result
            
