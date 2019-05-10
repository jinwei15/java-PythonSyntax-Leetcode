# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow, fast = head, head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        if slow == None or fast == None or slow != fast: return None
        ptr1, ptr2 = head, slow
        while (ptr1 != ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
