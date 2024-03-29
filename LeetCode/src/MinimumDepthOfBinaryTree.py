
   # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None :
            return 0
        if root.left == None and root.right == None :
            return 1
        if root.left == None:
            return minDepth(root.right) + 1
        if root.right == None:
            return minDepth(root.left) + 1
        
        return min(minDepth(root.left),minDepth(root.right)) + 1
    
# Driver Program  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print minDepth(root))         
