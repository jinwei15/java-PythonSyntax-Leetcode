# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        ptr1 = dummy
        ptr2 = dummy
        for _ in range(n + 1):
            ptr2 = ptr2.next

        while (ptr2 != None):
            ptr2 = ptr2.next
            ptr1 = ptr1.next

        ptr1.next = ptr1.next.next
        return dummy.next

# public ListNode removeNthFromEnd(ListNode head, int n) {
#     ListNode dummy = new ListNode(0);
#     dummy.next = head;
#     ListNode first = dummy;
#     ListNode second = dummy;
#     // Advances first pointer so that the gap between first and second is n nodes apart
#     for (int i = 1; i <= n + 1; i++) {
#         first = first.next;
#     }
#     // Move first to the end, maintaining the gap
#     while (first != null) {
#         first = first.next;
#         second = second.next;
#     }
#     second.next = second.next.next;
#     return dummy.next;
# }