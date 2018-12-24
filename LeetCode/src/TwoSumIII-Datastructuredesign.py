# Design and implement a TwoSum class. It should support the following operations: add and find.


# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.





# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Example 2:



# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.mapList = dict()
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums.append(number)
        self.mapList[number] = len(self.nums) - 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if len(self.nums) <= 1: return False
        for i in range(len(self.nums)):
            complement = value - self.nums[i]
            if self.mapList.get(complement) != None and self.mapList.get(complement)!= i:
                # return [mapList.get(complement),i]
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
