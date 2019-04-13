# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         result = list()
#         for row in range(numRows):
#             newList = list()
#             for index in range(row+1):
#                 newList.append(self.f(row,index))
#             result.append(newList)   
#         return result
            
    
#     def f(self,i,j):
#         if i == 0 or j == 0 or i == j:
#             return 1
#         else:
#             return self.f(i-1,j-1) + self.f(i-1,j)
            
        
        
        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        for row in range(numRows):
            newList = list()
            for index in range(row+1):
                if index == 0 or index == row :
                    newList.append(1)
                else:
                    newList.append(result[row-1][index-1]+result[row-1][index])
            result.append(newList)
        return result
                
