# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        currA = headA
        currB = headB
        while(currA is not currB):
            currA = headB if currA == None else currA.next
            currB = headA if currB == None else currB.next
#             if currA == None:
#                 currA = headB
#             else:
#                 currA = currA.next
                
#             if currB == None:
#                 currB = headA
#             else:
#                 currB = currB.next
        
        return currA
                
        
