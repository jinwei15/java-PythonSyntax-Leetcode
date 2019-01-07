class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        #slicing window solution
        # explaination: we have a window only increase size never shrik size. 
        # window will increase from 0 to a size at the beginning. the end of the window becomes the 
        # the head of another window then check all element within the size of the windw increase the size
        # if needed. So that with only one scan we are able to tell the max output 
        
        #now start implement:
#         if tree == None: return None
#         if len(tree) == 1: return 1
        
#         winLen = 0
#         winHead = 0
#         length = len(tree)
        
#         while(winHead + winLen < length): #edge case need to be considered
#             cur = winHead 
#             eleSet = set(tree[cur:cur + winLen])
#             while(len(eleSet) <= 2 and cur < length ):
#                 eleSet.add(tree[cur])
#                 cur += 1
#             if cur == length and cur - winHead > winLen and len(eleSet) <= 2:
#                     winLen = cur - winHead     
#             elif cur - winHead -1  > winLen:
#                 winLen = cur - winHead -1
#             winHead += 1
        
#         return winLen
            

        ans = i = 0
        count = collections.Counter()
        for index, value in enumerate(tree):
            count[value] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, index - i + 1)
        return ans
            
