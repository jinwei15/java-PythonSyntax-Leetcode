"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         def helper(root):

#             if root == None:
#                 return
#             res.append(root.val)
#             for child in root.children:
#                 helper(child)
#         helper(root)
#         return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(root):

            if root == None:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)

        helper(root)
        return res

# class Solution {
#     public List<Integer> preorder(Node root) {
#         List<Integer> list = new ArrayList<>();
#         if (root == null) return list;

#         Stack<Node> stack = new Stack<>();
#         stack.add(root);

#         while (!stack.empty()) {
#             root = stack.pop();
#             list.add(root.val);
#             for (int i = root.children.size() - 1; i >= 0; i--)
#                 stack.add(root.children.get(i));
#         }

#         return list;
#     }
# }
