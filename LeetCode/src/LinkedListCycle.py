# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#using hashmap loop through the linked list one by one
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         #assume there is no cycle
#         flag = False
#         hist = dict()
#         while(head != None):
#             hist[head] = hist.get(head,0) + 1
#             if hist[head] == 2:
#                 flag = True
#                 break
#             else:
#                 head = head.next
        
#         return flag




#second way is to use two pointer one move 1 step per time the other one moves 2 steps per time.
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #assume there is no cycle
        if (head == None or head.next == None) :
            return False
    
        slow = head
        fast = head.next
        while (slow != fast):
            if (fast == None or fast.next == None) :
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
