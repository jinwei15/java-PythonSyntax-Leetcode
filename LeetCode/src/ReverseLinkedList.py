# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         #put everying in a list
#         numberList = list()
#         while (head != None):
#             numberList.append(head.val)
#             head = head.next
        
#         # reverse the list
#         newList = numberList[::-1]
        
#         if len(newList) == 0: return None
#         #create a new List node.
#         newhead = ListNode(newList[0])
#         current = newhead
#         for i in range(1,len(newList)):
            
#             node = ListNode(newList[i])
#             current.next = node
#             current = current.next
        
#         return newhead
        prev = None
        curr = head
        while(curr != None):
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
   
