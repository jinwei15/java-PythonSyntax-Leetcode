# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

 

# Example 1:


# Input: [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: [2,2,2,5,2]
# Output: false
 

# Note:

# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        self.val = root.val
        
        return self.dfs(root)
        
        
    def dfs(self,root):
        if root == None:
            return True
        else:
            if root.val != self.val:
                return False
        
        return self.dfs(root.left) and self.dfs(root.right)
        
        
            
        
