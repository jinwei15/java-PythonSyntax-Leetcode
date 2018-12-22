# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sol = ListNode(0)
        curr = sol
        p = self.reverseList(l1)
        q = self.reverseList(l2)
        carry = 0

        while p != None or q != None:

            if p != None:
                x = p.val
            else:
                x = 0

            if q != None:
                y = q.val
            else:
                y = 0

            sum = x + y + carry

            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if p != None:
                p = p.next
            else:
                p = None

            if q != None:
                q = q.next
            else:
                q = None

        if carry > 0:
            curr.next = ListNode(carry)

        return self.reverseList(sol.next)





#7 -> 2 -> 4 -> 3 -> None

#3 -> 4 -> 2 -> 7 -> None
    def reverseList(self,head):
        prevNode = None
        currNode = head
        while(currNode != None):
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp
        return prevNode
        
        
        
