class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S = self.deleteHash(S)
        T = self.deleteHash(T)
        print(S)
        print(T)
        return S==T
    
    def deleteHash(self,Str):
        while '#' in Str:
            index = Str.find('#')
            if index - 1 >= 0:
                Str = Str[:index-1] + Str[index+1:]
            else:
                Str =  Str[index+1:]
        return Str
    
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)


