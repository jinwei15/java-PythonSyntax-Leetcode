# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head==None or head.next==None:
            return head
        
        temp = head.next
        
        head.next = self.swapPairs(head.next.next)
        
        temp.next = head
        
        return temp
        
        
        

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
        
#         curr = dummy

#         while(curr.next != None and curr.next.next!=None):
#             first = curr.next
#             second = curr.next.next
#             curr.next  = second
#             first.next = second.next
#             second.next = first
#             curr = curr.next.next
            
            
#         return dummy.next 
            
        
