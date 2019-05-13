# Input: {"$id": "1",
#         "left": {"$id": "2",
#                  "left": {"$id": "3",
#                           "left": null,
#                           "next": null,
#                           "right": null,
#                           "val": 4},
#                  "next": null,
#                  "right": {"$id": "4",
#                            "left": null,
#                            "next": null,
#                            "right": null,
#                            "val": 5},
#                  "val": 2},
#         "next": null,
#         "right": {"$id": "5",
#                   "left": {"$id": "6",
#                            "left": null,
#                            "next": null,
#                            "right": null,
#                            "val": 6},
#                   "next": null,
#                   "right": {"$id": "7",
#                             "left": null,
#                             "next": null,
#                             "right": null,
#                             "val": 7},
#                   "val": 3},
#         "val": 1}
#
# Output: {"$id": "1",
#          "left": {"$id": "2",
#                   "left": {"$id": "3",
#                            "left": null,
#                            "next": {"$id": "4",
#                                     "left": null,
#                                     "next": {"$id": "5",
#                                              "left": null,
#                                              "next": {"$id": "6",
#                                                       "left": null,
#                                                        "next": null,
#                                                        "right": null,
#                                                        "val": 7},
#                                              "right": null, "val": 6},
#                                     "right": null, "val": 5},
#                            "right": null, "val": 4},
#                   "next": {"$id": "7",
#                            "left": {"$ref": "5"},
#                            "next": null,
#                            "right": {"$ref": "6"},
#                             "val": 3},
#                             "right": {"$ref": "4"},
#                   "val": 2},
#          "next": null,
#          "right": {"$ref": "7"},
#          "val": 1}

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
        if root==None:
            return
        if (root.left != None):
            root.left.next = root.right
            if (root.next != None):
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
