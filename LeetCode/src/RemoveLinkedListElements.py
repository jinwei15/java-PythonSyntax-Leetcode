# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        previous = None
        while(current!=None and head!= None):
            if current.val == val:
                if previous == None:
                    head = head.next
                    current = head
                else:
                    previous.next = current.next
                    current = current.next
            elif current.val != val:
                previous = current
                current = current.next
        return head

            
        
