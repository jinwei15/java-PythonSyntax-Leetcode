# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root):
            if root == None:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            if (left == right):
                if (root.left != None and root.left.val != root.val): return False
                if (root.right != None and root.right.val != root.val): return False
                self.count += 1
                return True
            else:
                return False

        dfs(root)
        return self.count

# public class Solution {
#     public int countUnivalSubtrees(TreeNode root) {
#         int[] arr = new int[1];
#         postOrder(arr, root);
#         return arr[0];
#     }
#     public boolean postOrder (int[] arr, TreeNode node) {
#         if (node == null) return true;
#         boolean left = postOrder(arr, node.left);
#         boolean right = postOrder(arr, node.right);
#         if (left && right) {
#             if (node.left != null && node.left.val != node.val) return false;
#             if (node.right != null && node.right.val != node.val) return false;
#             arr[0]++;
#             return true;
#         }
#         return false;
#     }
# }

