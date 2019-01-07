ass LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.queue = collections.deque()
        self.dic = dict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        #deque is python is implementated by doublelinked list so that remove will take constant time
        if key in self.dic:
            self.queue.remove(key)
            self.queue.append(key)  
        return self.dic.get(key,-1)
    
        

#    def put(self, key, value): # this is wrong see below
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         # if key not in self.dic:
        
#         self.queue.append(key)
#         if len(self.queue) > self.cap:
#             print(self.queue)
#             print(key, value)
#             headKey = self.queue.popleft()
#             if headKey in self.dic:
#                 del self.dic[headKey]
#         self.dic[key] = value
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:    
            self.queue.remove(key)
        self.queue.append(key)
        self.dic[key] = value 
        
        if len(self.dic) > self.cap:
            v = self.queue.popleft()  # remove the Least Recently Used element
            self.dic.pop(v)
        
        

        


# # # Your LRUCache object will be instantiated and called as such:
# # # obj = LRUCache(capacity)
# # # param_1 = obj.get(key)
# # # obj.put(key,value)

# class Node:
#     def __init__(self, k, v):
#         self.key = k
#         self.val = v
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.dic = dict()
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key):
#         if key in self.dic:
#             n = self.dic[key]
#             self.remove(n)
#             self.add(n)
#             return n.val
#         return -1

#     def put(self, key, value):
#         if key in self.dic:
#             self.remove(self.dic[key])
#         n = Node(key, value)
#         self.add(n)
#         self.dic[key] = n
#         if len(self.dic) > self.capacity:
#             n = self.head.next
#             self.remove(n)
#             del self.dic[n.key]

#     def remove(self, node):
#         p = node.prev
#         n = node.next
#         p.next = n
#         n.prev = p

#     def add(self, node):
#         p = self.tail.prev
#         p.next = node
#         self.tail.prev = node
#         node.prev = p
#         node.next = self.tail
