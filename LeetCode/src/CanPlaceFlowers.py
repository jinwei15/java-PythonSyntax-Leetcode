# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: return True
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n ==1:
            return True
        for i in range(len(flowerbed)):
            # if i == 0 and i+1<len(flowerbed) and flowerbed[i+1] == 0 and flowerbed[i] == 0:
            #     flowerbed[i] = 1
            #     n = n -1
            # if i == len(flowerbed)-1 and i-1 >= 0 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
            #     flowerbed[i] = 1
            #     n = n -1
            
            left = i - 1
            right = i + 1
            
            if left >= 0 and right < len(flowerbed):
                if flowerbed[left] == 0 and flowerbed[right] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n = n -1
                    
            elif left == -1 and right < len(flowerbed):
                if flowerbed[right] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n = n -1
                
                
            elif left >= 0 and right == len(flowerbed):
                 if flowerbed[left] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n = n -1
            if n == 0: return True 
                
        return False
            
                
                
    
    
#     def validSlot(listSlot):
#         """
#         return how many valid slots are there in the list
#         """
        
        
