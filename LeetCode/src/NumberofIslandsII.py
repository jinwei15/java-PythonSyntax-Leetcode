class Solution:
    def numIslands2(self, m: 'int', n: 'int', positions: 'List[List[int]]') -> 'List[int]':
        self.grid = [['0' for _ in range(n)] for _ in range(m)]
        res = []
        for pair in positions:
            i = pair[0]
            j = pair[1]
            self.grid[i][j] = '1'
            new = self.copyGrid(m, n, self.grid)
            res.append(self.numIslandsConversion(self.grid))
            self.grid = new
        return res

    def copyGrid(self, m, n, grid):
        copy = [['0' for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                copy[i][j] = grid[i][j]
        return copy

    def numIslandsConversion(self, grid: 'List[List[str]]') -> 'int':
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
                    queue.append((r, c))
                    grid[r][c] = '0'  # mark as 0
                    while (len(queue) != 0):
                        (row, col) = queue.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            queue.append((row - 1, col))
                            grid[row - 1][col] = '0'
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            queue.append((row + 1, col))
                            grid[row + 1][col] = '0'
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            queue.append((row, col - 1))
                            grid[row][col - 1] = '0'
                        if col + 1 < nc and grid[row][col + 1] == '1':
                            queue.append((row, col + 1))
                            grid[row][col + 1] = '0'

        return num_island
