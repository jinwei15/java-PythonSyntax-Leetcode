#
#
#
#
#
# 3. subtree:  maximum average node (https://yeqiuquan.blogspot.com/2017/03/lintcode-597-subtree-with-maximum.html)
#
# ..多叉树最大子树平均。地里有，我的变种是平均不带自己。比如树
#     4
#   /  |  \
# 1  2  3
# 这样的情况4这个node的平均是 （1+2+3）/3 而不是 （1+2+3+4）/ 4
#
# Tree里面找所有node平均值最大的子树，输出root. （leave node不算子树。）
#
# ..结点+他的子树/结点个数 的最大值。第二题我用的bottom up，迷之test case有几个一直过不了，又看不到test case内容，又不能自己定义test case来测试
#
# ..最大子tree node值的平均值。在北美读的大学实在不知道怎么用中文描述请谅解。注意不是binary tree。其实直接backtrack就好。
#
# ..愚蠢的想问一下第二题的testcase 1:
# 1->2->3
# expected answer: 2
# 为什么不是3 因为除去leaf node
#
# ..maximum average subtree，这个tree是N-ary tree。
# 求每个node以及其所有后代的value平均值，返回平均值最大的node
#
#
# ..2. maximum average subtree
# https://yeqiuquan.blogspot.com/2 ... e-with-maximum.html
# 我照着这个链接的方法写的
# 真正题目里面每个node有好几个子节点
# 需要注意叶子结点不能作为结果
#
#
# ..第二题最近高频的n叉树找最大的sum/node数的结点，dfs就完了，注意要排除叶子结点。

# https://yeqiuquan.blogspot.com/2017/03/lintcode-597-subtree-with-maximum.html
#
# Description
# Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
#
# Notice
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum average.
#
#
# Example
# Given a binary tree:
#
#      1
#     /   \
#  -5     11
#  / \     /  \
# 1   2 4    -2
#
# return the node 11.
#
# 思路
# 这一类的题目都可以这样做：
# 开一个ResultType的变量result，来储存拥有最大average的那个node的信息。
# 然后用分治法来遍历整棵树。
# 一个小弟找左子数的average，一个小弟找右子树的average。然后通过这两个来计算当前树的average。同时，我们根据算出来的当前树的average决定要不要更新result。
# 当遍历完整棵树的时候，result里记录的就是拥有最大average的子树的信息。


# ..maximum average subtree，这个tree是N-ary tree。
# 求每个node以及其所有后代的value平均值，返回平均值最大的node
import sys


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def mas (self, root):
        if root is None:
            return None

        self.max_average = -sys.maxsize
        self.node = None
        self.find_max_average(root)

        return self.node

    def find_max_average(self, root):
        if len(root.children) == 0:
            if root.val > self.max_average:
                self.max_average = root.val
                self.node = root
            return 1, root.val

        count, sum = 0, 0
        for child in root.children:
            c_count, c_sum = self.find_max_average(child)
            count += c_count
            sum += c_sum

        if sum / count > self.max_average:
            self.max_average = sum / count
            self.node = root

        return sum, count




bb = Solution()
## case 1:
leaf1 = [Node(3, []), Node(4, [])]
leaf2 = [Node(6, []), Node(7, [])]
leaf3 = [Node(1, []), Node(10, [])]
c1 = Node(1, leaf1)
c2 = Node(2, leaf2)
c3 = Node(3, leaf3)
root = Node(4, [c1, c2, c3])


## case2
root = Node(4,[])
result = bb.mas(root)

print(result.val)























#
#
#
# import sys
#
#
# # Definition for a Node.
# class Node:
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children
#
# class Solution:
#     def mas (self, root):
#         if root is None:
#             return None
#
#         self.max_average = -sys.maxsize
#         self.node = None
#         self.find_max_average(root)
#
#         return self.node
#
#     def find_max_average(self, root):
#         if len(root.children) == 0:
#             if root.val > self.max_average:
#                 self.max_average = root.val
#                 self.node = root
#             return root.val, 1
#
#         count, sum = 1, root.val
#         for child in root.children:
#             c_count, c_sum = self.find_max_average(child)
#             count += c_count
#             sum += c_sum
#
#         if sum / count > self.max_average:
#             self.max_average = sum / count
#             self.node = root
#
#         return sum, count





