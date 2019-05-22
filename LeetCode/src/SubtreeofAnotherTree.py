# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isSame(t1, t2):
            if t1 == None and t2 == None: return True
            if t1 == None or t2 == None: return False
            if t1.val != t2.val: return False
            return isSame(t1.left, t2.left) and isSame(t1.right, t2.right);

        if s == None: return False
        if isSame(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# public class Solution {
#     public boolean isSubtree(TreeNode s, TreeNode t) {
#         if (s == null) return false;
#         if (isSame(s, t)) return true;
#         return isSubtree(s.left, t) || isSubtree(s.right, t);
#     }
#     private boolean isSame(TreeNode s, TreeNode t) {
#         if (s == null && t == null) return true;
#         if (s == null || t == null) return false;
#         if (s.val != t.val) return false;
#         return isSame(s.left, t.left) && isSame(s.right, t.right);
#     }
# }