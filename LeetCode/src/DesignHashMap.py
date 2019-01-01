class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyList = []
        self.valueList = []
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.keyList:
            i = self.keyList.index(key)
            self.valueList[i] = value
        else:
            self.keyList.append(key)
            self.valueList.append(value)
            
            

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.keyList:
            i = self.keyList.index(key)
            return self.valueList[i]
        else:
            return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if key in self.keyList:
            i = self.keyList.index(key)
            del self.keyList[i]
            del self.valueList[i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# class MyHashMap(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.table = [-1] * 1000001

#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         self.table[key] = value
        

#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         return self.table[key]
        

#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: void
#         """
#         self.table[key] = -1


# # Your MyHashMap object will be instantiated and called as such:
# # obj = MyHashMap()
# # obj.put(key,value)
# # param_2 = obj.get(key)
# # obj.remove(key)
