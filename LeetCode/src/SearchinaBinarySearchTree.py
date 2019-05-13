# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while (root != None):
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None

# class Solution {
#     public TreeNode searchBST(TreeNode root, int target) {
#         if (root == null || root.val == target) {
#             return root;
#         }
#         if (target < root.val) {
#             return searchBST(root.left, target);
#         }else{
#             return searchBST(root.right, target);
#         }
#     }
# }