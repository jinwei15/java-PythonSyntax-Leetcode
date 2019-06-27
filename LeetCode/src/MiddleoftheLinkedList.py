# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pointer1 = head
        pointer2 = head
        while (pointer2 != None and pointer2.next != None):
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        return pointer1


# this is the runner technique which is the two pointer technique.