# ou are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution:
#     def islandPerimeter(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         row = len(grid)
#         col = len(grid[0])
#         bigGrid = [[0 for x in range(col+2)] for y in range(row+2)] 
        
#         for i in range(row):
#             for j in range(col):
#                 bigGrid[i+1][j+1] = grid[i][j]
        
#         # print(bigGrid)
        
#         result = 0 
#         for i in range(1,row+1):
#             for j in range(1,col+1):
#                 # up = i -1 
#                 # down = i + 1
#                 # left = j - 1
#                 # right = j + 1
#                 temp = 4
#                 if bigGrid[i][j] == 1:
#                     sumAll = bigGrid[i -1][j]+bigGrid[i + 1][j]+bigGrid[i][j-1]+bigGrid[i][j+1]
#                     temp -= sumAll
#                     result += temp
#         return result
   def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or grid[0] == None:
            return 0
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += 4
                    if (i>0 and grid[i-1][j] == 1): result -= 2
                    if (j>0 and grid[i][j-1] == 1): result -= 2
        return result

                        
                    
                    
                
# public static int islandPerimeter(int[][] grid) {
#         if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
#         int result = 0;
#         for (int i = 0; i < grid.length; i++) {
#             for (int j = 0; j < grid[0].length; j++) {
#                 if (grid[i][j] == 1) {
#                     result += 4;
#                     if (i > 0 && grid[i-1][j] == 1) result -= 2;
#                     if (j > 0 && grid[i][j-1] == 1) result -= 2;
#                 }
#             }
#         }
#         return result;
#     }
