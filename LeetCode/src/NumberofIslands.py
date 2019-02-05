# class Land:
#     """
#     the island which has a string value and a island value.  
#     """

#     def __init__(self, val, island_No):
#         self.val = val
#         self.island = island_No


# class Solution:
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         isLand_no = 0


#         row = len(grid)
#         if not row: return isLand_no
#         column = len(grid[0])
#         nodes = [[Land('0',0) for j in range(column)] for i in range(row)]
#         for i in range(row):
#             for j in range(column):
#                 if grid[i][j] == '1':
#                     up = i - 1
#                     down = i + 1
#                     right = j + 1
#                     left = j - 1

#                     if (up >= 0 and nodes[up][j].val == '1') or \
#                             (down < row and nodes[down][j].val == '1') or \
#                             (right < column and nodes[i][right].val == '1') or \
#                             (left >= 0 and nodes[i][left].val == '1'):
#                         nodes[i][j] = Land(grid[i][j], isLand_no)

#                     else:
#                         isLand_no += 1
#                         nodes[i][j] = Land(grid[i][j], isLand_no)

#         return isLand_no


# bb = Solution()
# print(bb.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

# the above example is wrong!

class Solution:
    
    def dfs(self,grid,r, c):
        nr = len(grid)
        nc = len(grid[0])

        if (r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0'):
          return 

        grid[r][c] = '0'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if (grid == None or len(grid) == 0):
          return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr) :
          for c in range(nc):
            if (grid[r][c] == '1') :
              num_islands+=1
              self.dfs(grid, r, c)


    

        return num_islands;
    
class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if grid == None or len(grid) == 0:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        num_island = 0
        queue = collections.deque()
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_island += 1
                    
                    queue.clear()
                    queue.append((r,c))
                    grid[r][c] = '0' # mark as 0
                    while(len(queue) != 0):
                        (row, col) = queue.popleft()
                        if row - 1 >= 0 and grid[row-1][col] == '1':
                            queue.append((row -1,col))
                            grid[row-1][col] = '0'
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            queue.append((row+1,col))
                            grid[row+1][col] = '0'
                        if col - 1 >= 0 and grid[row][col -1] == '1':
                            queue.append((row,col-1))
                            grid[row][col-1] = '0'
                        if col + 1 < nc and grid[row][col +1] == '1':
                            queue.append((row,col+1))
                            grid[row][col+1] = '0'
                            
                        
                        
        return num_island
                        
  


