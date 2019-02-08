# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.visited = dict()

    def getClonedNode(self, node):
        # If node exists then
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        else:
            return None

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None: return None

        old_node = head
        # Creating the new head node.
        new_node = RandomListNode(old_node.label)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:
            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]