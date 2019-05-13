# # input {"$id": "1",
# "left": {"$id": "2",
#          "left": {"$id": "3",
#                   "left": {"$id": "4",
#                            "left": null,
#                            "next": null,
#                            "right": null,
#                            "val": 2},
#                   "next": null,
#                   "right": null,
#                   "val": 0},
#          "next": null,
#          "right": {"$id": "5",
#                    "left": {"$id": "6",
#                             "left": null,
#                             "next": null,
#                             "right": null,
#                             "val": 1},
#                    "next": null,
#                    "right": {"$id": "7",
#                              "left": {"$id": "8",
#                                       "left": null,
#                                       "next": null,
#                                       "right": null,
#                                       "val": 7},
#                              "next": null,
#                              "right": null,
#                              "val": 0},
#                    "val": 7},
#          "val": 1},
# "next": null,
# "right": {"$id": "9",
#           "left": {"$id": "10",
#                    "left": null,
#                    "next": null,
#                    "right": null,
#                    "val": 9},
#           "next": null,
#           "right": {"$id": "11",
#                     "left": {"$id": "12",
#                              "left": null,
#                              "next": null,
#                              "right": null,
#                              "val": 8},
#                     "next": null,
#                     "right": {"$id": "13",
#                               "left": null,
#                               "next": null,
#                               "right": null,
#                               "val": 8},
#                     "val": 1},
#           "val": 3},
# "val": 2}
#
# # out {"$id": "1",
#        "left": {"$id": "2",
#                 "left": {"$id": "3",
#                          "left": {"$id": "4",
#                                   "left": null,
#                                   "next": {"$id": "5",
#                                            "left": null,
#                                            "next": {"$id": "6",
#                                                     "left": { "$id": "7",
#                                                               "left": null,
#                                                               "next": null,
#                                                               "right": null,
#                                                               "val": 7},
#                                                     "next": null,
#                                                     "right": null,
#                                                     "val": 0},
#                                             "right": null,
#                                             "val": 1},
#                                   "right": null,
#                                   "val": 2},
#                          "next": {"$id": "8",
#                                   "left": {"$ref": "5"},
#                                             "next": {"$id": "9",
#                                                      "left": null,
#                                                      "next": {"$id": "10",
#                                                               "left": {
#                                                                   "$id": "11",
#                                                                   "left": null,
#                                                                   "next": {
#                                                                       "$id": "12",
#                                                                       "left": null,
#                                                                       "next": null,
#                                                                       "right": null,
#                                                                       "val": 8},
#                                                                   "right": null,
#                                                                   "val": 8},
#                                                               "next": null,
#                                                               "right": {
#                                                                   "$ref": "12"},
#                                                               "val": 1},
#                                                      "right": null, "val": 9},
#                                             "right": {"$ref": "6"}, "val": 7},
#                                            "right": null, "val": 0},
#                       "next": {"$id": "13", "left": {"$ref": "9"}, "next": null, "right": {"$ref": "10"}, "val": 3},
#                       "right": {"$ref": "8"}, "val": 1}, "next": null, "right": {"$ref": "13"}, "val": 2}
#
# {"$id": "1", "left": {"$id": "2", "left": {"$id": "3", "left": {"$id": "4", "left": null,
#                                                                 "next": {"$id": "5", "left": null, "next": {"$id": "6",
#                                                                                                             "left": {
#                                                                                                                 "$id": "7",
#                                                                                                                 "left": null,
#                                                                                                                 "next": null,
#                                                                                                                 "right": null,
#                                                                                                                 "val": 7},
#                                                                                                             "next": {
#                                                                                                                 "$id": "8",
#                                                                                                                 "left": null,
#                                                                                                                 "next": {
#                                                                                                                     "$id": "9",
#                                                                                                                     "left": null,
#                                                                                                                     "next": null,
#                                                                                                                     "right": null,
#                                                                                                                     "val": 8},
#                                                                                                                 "right": null,
#                                                                                                                 "val": 8},
#                                                                                                             "right": null,
#                                                                                                             "val": 0},
#                                                                          "right": null, "val": 1}, "right": null,
#                                                                 "val": 2}, "next": {"$id": "10", "left": {"$ref": "5"},
#                                                                                     "next": {"$id": "11", "left": null,
#                                                                                              "next": {"$id": "12",
#                                                                                                       "left": {
#                                                                                                           "$ref": "8"},
#                                                                                                       "next": null,
#                                                                                                       "right": {
#                                                                                                           "$ref": "9"},
#                                                                                                       "val": 1},
#                                                                                              "right": null, "val": 9},
#                                                                                     "right": {"$ref": "6"}, "val": 7},
#                                            "right": null, "val": 0},
#                       "next": {"$id": "13", "left": {"$ref": "11"}, "next": null, "right": {"$ref": "12"}, "val": 3},
#                       "right": {"$ref": "10"}, "val": 1}, "next": null, "right": {"$ref": "13"}, "val": 2}
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = []

        def levelOrder(root, depth):
            if root == None:
                return
            if depth >= len(res):
                res.append([])
            res[depth].append(root)
            levelOrder(root.left, depth + 1)
            levelOrder(root.right, depth + 1)

        levelOrder(root, 0)

        def reconnect(root, depth):
            if root == None:
                return
            index = res[depth].index(root)
            if index < len(res[depth]) - 1:
                root.next = res[depth][index + 1]

            reconnect(root.left, depth + 1)
            reconnect(root.right, depth + 1)

            return root

        return reconnect(root, 0)

# public class Solution {
#     public void connect(TreeLinkNode root) {

#         while(root != null){
#             TreeLinkNode tempChild = new TreeLinkNode(0);
#             TreeLinkNode currentChild = tempChild;
#             while(root!=null){
#                 if(root.left != null) { currentChild.next = root.left; currentChild = currentChild.next;}
#                 if(root.right != null) { currentChild.next = root.right; currentChild = currentChild.next;}
#                 root = root.next;
#             }
#             root = tempChild.next;
#         }
#     }
# }

