#implement the fix sized queue with an array (fixed sized), this is my own implemntation
# the idea was that to to it as a double linked list and them keep tracking the head and the tail
# also keep tracking the length so that we cal always add by O(1) and pop by O(1)
class Node:
    def __init__(self,x):
        self.val = x
        self.pre = None
        self.next = None

class fixedSize:
    def __init__(self,maxSize):
        self.length = 0
        self.head = None
        self.past = None
        self.maxSize = maxSize
    
    def push(self,x):
        if self.head == None:
            self.head = Node(x)
            self.past = self.head
            self.length += 1
        
        elif self.length<self.maxSize:
            self.length += 1
            new = Node(x)
            new.pre = self.past
            self.past.next = new
            self.past = self.past.next
        else:
            self.pop()
            self.push(x)


                            
    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            value = self.head.val
            self.head = None
            self.pst = None
            self.length -= 1
            return value
            
        else:
            self.length -= 1
            value = self.head.val
            temp = self.head.next
            self.head.next = None
            self.head = temp
            self.head.pre = None
            return value
        

    def printList(self):
        curr = self.head
        print('length of list is :', self.length)
        while(curr):
            print(curr.val)
            curr = curr.next
            
    
#test = fixedSize(5)
#test.push(2)
#test.push(3)
#test.push(4)
#test.push(5)
#test.push(6)
#test.push(7)
#
#
#test.printList()
#

class FixedQueue2():

    def __init__(self,k):
        self.arr = [None for _ in range(k)]
        self.end = 0
        self.start = 0
        self.k = k
        self.length = 0


    def push(self, x):
        if self.length < self.k:
            self.arr[self.end] = x
            self.length += 1
            self.end = (self.end + 1) % self.k
        else: # case length >= k
            self.pop()
            self.push(x)

    def pop(self):
        if self.start == self.end:
            return 
        else:
            returnVal = self.arr[self.start]
            self.start = (self.start + 1) % self.k
            return returnVal
    def printAll(self):
        i = self.start
        
            
        print(self.arr[self.start:]+self.arr[self.end:self.start])


sol = FixedQueue2(5)
sol.push(1)
sol.push(2)
sol.push(4)
sol.push(6)
sol.push(7)
sol.push(9)

sol.printAll()
