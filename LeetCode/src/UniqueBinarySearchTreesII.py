# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def helper(start, end):
            listRoot = list()
            if start >end:
                return [None]
            
            for i in range(start,end+1):
                leftNodes = helper(start,i-1)
                rightNodes = helper(i+1,end)
                
                for l in leftNodes:
                    for r in rightNodes:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        listRoot.append(curr)
            
            return listRoot
        return helper(1, n) if n else []
        
