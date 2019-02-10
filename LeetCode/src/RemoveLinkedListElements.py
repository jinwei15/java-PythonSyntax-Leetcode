# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return []

        fakeHead = ListNode(0)
        fakeHead.next = head

        curr = head
        pre = fakeHead

        while curr != None:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next

        return fakeHead.next

# public class Solution {
#     public ListNode removeElements(ListNode head, int val) {
#         ListNode fakeHead = new ListNode(-1);
#         fakeHead.next = head;
#         ListNode curr = head, prev = fakeHead;
#         while (curr != null) {
#             if (curr.val == val) {
#                 prev.next = curr.next;
#             } else {
#                 prev = prev.next;
#             }
#             curr = curr.next;
#         }
#         return fakeHead.next;
#     }
# }