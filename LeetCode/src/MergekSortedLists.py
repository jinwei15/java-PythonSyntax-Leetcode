# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# using heap to merge


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        1. 需要提前给一个point 的head copy
        2. 将所有的node放入一个list 里然后sort
        3. 将sort 好的list 重新 建立一个 listnode
        4. 根据1 的head 将好的list node 返回
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

# from heapq import *
# class Solution():
#     def mergeKLists(self,lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         head = point = ListNode(0)
#         hp = []
#         for i in range(len(lists)):
#             if lists[i]:
#                 heappush(hp, (lists[i].val, lists[i]))
#         while(len(hp)>0):
#             val, node = heappop()
#             point.next = ListNode(val)
#             point = point.next
#             node = node.next
#             if node:
#                 heappush(hp,(nodeLi.val,nodeLi))
#         return head.next

