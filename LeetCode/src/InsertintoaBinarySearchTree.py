# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # dummy = TreeNode(-1)
        dummy = root
        while (root != None):
            if val == root.val:
                return root
            elif val < root.val:
                if root.left != None:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            elif val > root.val:
                if root.right != None:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
        return dummy

# class Solution {
#     public TreeNode insertIntoBST(TreeNode root, int val) {
#         if (root == null) {
#             return new TreeNode(val);   // return a new node if root is null
#         }
#         if (root.val < val) {           // insert to the right subtree if val > root->val
#             root.right = insertIntoBST(root.right, val);
#         } else {                        // insert to the left subtree if val <= root->val
#             root.left = insertIntoBST(root.left, val);
#         }
#         return root;
#     }
# }