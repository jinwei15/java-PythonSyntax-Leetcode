# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # two pointer solutions
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        before = ListNode(-1)
        after = ListNode(-1)

        currAfter = after
        currBefore = before

        while (head):
            if head.val < x:
                currBefore.next = head
                currBefore = head
            else:  # val >= x
                currAfter.next = head
                currAfter = head

            head = head.next

        currAfter.next = head
        currBefore.next = after.next

        return before.next


