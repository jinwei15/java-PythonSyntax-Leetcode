class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
#         banSet = set(banned)
#         value = 0
#         wordDict = dict()
#         paragraphList = list(paragraph)
#         for i in range(len(paragraphList)):
#             if not paragraphList[i].isalpha():
#                 paragraphList[i] = ' '
#         paragraph = ''.join(paragraphList)
#         words = paragraph.split()
#         print(words)
#         for i in range(len(words)):
#             wordDict [words[i].lower()] = wordDict.get(words[i].lower(),0) + 1
        
#         for k,v in wordDict.items():
#             if k not in banSet and v > value:
#                 value = v
#                 ans = k
#         return ans
        
    
    
        banSet = set(banned)
        value = 0
        wordDict = dict()
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace(":", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("'", " ")
        words = paragraph.split()
        print(words)
        for i in range(len(words)):
            wordDict [words[i].lower()] = wordDict.get(words[i].lower(),0) + 1
        
        for k,v in wordDict.items():
            if k not in banSet and v > value:
                value = v
                ans = k
        return ans
        
