class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.head.next = self.tail
        self.head.prev = None

        self.tail = Node(-1)
        self.tail.prev = self.head
        self.tail.next = None

        self.length = 0

    def get(self, index: 'int') -> 'int':
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
            if curr == None:
                return -1
        return curr

    def addAtHead(self, val: 'int') -> 'None':
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        temp = self.head.next
        temp.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = temp

    def addAtTail(self, val: 'int') -> 'None':
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        temp = self.tail.prev
        temp.next = newNode
        self.tail.prev = newNode
        newNode.prev = temp
        newNode.next = self.tail

    def addAtIndex(self, index: 'int', val: 'int') -> 'None':
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
            if curr == None:
                return -1
        return curr

    def deleteAtIndex(self, index: 'int') -> 'None':
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)