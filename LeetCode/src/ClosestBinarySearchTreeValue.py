# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: 'TreeNode', target: 'float') -> 'int':
        if root == None: return None

        self.dis = sys.maxsize
        self.result = None
        if self.dis > abs(root.val - target):
            self.dis = abs(root.val - target)
            self.result = root.val

        def dfs(root, target, result):
            if root == None: return

            if self.dis > abs(root.val - target):
                self.dis = abs(root.val - target)
                self.result = root.val

            dfs(root.left, target, self.result)
            dfs(root.right, target, self.result)

        dfs(root.left, target, self.result)
        dfs(root.right, target, self.result)

        return self.result


# public int closestValue(TreeNode root, double target) {
#     int ret = root.val;
#     while(root != null){
#         if(Math.abs(target - root.val) < Math.abs(target - ret)){
#             ret = root.val;
#         }
#         root = root.val > target? root.left: root.right;
#     }
#     return ret;
# }
root = TreeNode(1)
root.right = TreeNode(2)

Solution().closestValue(root,3.42)