# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.resList = []
        self.pointer = 0

        def convert(root):
            if root == None:
                return
            convert(root.left)
            self.resList.append(root.val)
            convert(root.right)

        convert(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """

        if self.hasNext():
            ret = self.resList[self.pointer]
            self.pointer += 1
            return ret

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.pointer < len(self.resList):
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()