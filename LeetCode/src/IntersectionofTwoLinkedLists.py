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
        visited = set()

        while (headA is not headB):

            if headA:
                if headA in visited:
                    return headA
                else:
                    visited.add(headA)
                    headA = headA.next

            if headB:
                if headB in visited:
                    return headB
                else:
                    visited.add(headB)
                    headB = headB.next

        # If headA and headB are equal
        return headA

#         def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         if headA is None or headB is None:
#             return None

#         currA = headA
#         currB = headB
#         while(currA is not currB):
#             currA = headB if currA == None else currA.next
#             currB = headA if currB == None else currB.next

#         return currA

