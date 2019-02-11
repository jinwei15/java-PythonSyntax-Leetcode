class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> 'int':
        if grid == None or len(grid) == 0:
            return 0
        seen = list()
        nr = len(grid)
        nc = len(grid[0])

        queue = collections.deque()

        for r in range(nr):
            for c in range(nc):
                islandTemp = list()
                if grid[r][c] == '1':

                    queue.clear()
                    queue.append((r, c))
                    islandTemp.add((r, c))
                    grid[r][c] = '0'  # mark as 0
                    while (len(queue) != 0):
                        (row, col) = queue.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            queue.append((row - 1, col))
                            grid[row - 1][col] = '0'
                            islandTemp.append((row - 1, col))
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            queue.append((row + 1, col))
                            grid[row + 1][col] = '0'
                            islandTemp.append((row + 1, col))
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            queue.append((row, col - 1))
                            grid[row][col - 1] = '0'
                            islandTemp.append((row, col - 1))
                        if col + 1 < nc and grid[row][col + 1] == '1':
                            queue.append((row, col + 1))
                            grid[row][col + 1] = '0'
                            islandTemp.append((row, col + 1))
                if len(islandTemp) != 0:
                    seen.append(islandTemp)
        self.findDistinct(seen)

    def findDistinct(self, seen: 'list(list())'):
        for i in seen:
            print(i)

# class Solution:
#     def numIslands(self, grid: 'List[List[str]]') -> 'int':
#         if grid == None or len(grid) == 0:
#             return 0

#         nr = len(grid)
#         nc = len(grid[0])
#         num_island = 0
#         queue = collections.deque()
#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == '1':
#                     num_island += 1

#                     queue.clear()
#                     queue.append((r,c))
#                     grid[r][c] = '0' # mark as 0
#                     while(len(queue) != 0):
#                         (row, col) = queue.popleft()
#                         if row - 1 >= 0 and grid[row-1][col] == '1':
#                             queue.append((row -1,col))
#                             grid[row-1][col] = '0'
#                         if row + 1 < nr and grid[row + 1][col] == '1':
#                             queue.append((row+1,col))
#                             grid[row+1][col] = '0'
#                         if col - 1 >= 0 and grid[row][col -1] == '1':
#                             queue.append((row,col-1))
#                             grid[row][col-1] = '0'
#                         if col + 1 < nc and grid[row][col +1] == '1':
#                             queue.append((row,col+1))
#                             grid[row][col+1] = '0'
#         return num_island
