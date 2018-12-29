import sys
class Solution:
    def findMaxMin(self, height):
        row, col = len(height), len(height[0])
        dp = [[-sys.maxsize-1 for i in range(col + 1)] for j in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if i == 1 and j == 1:
                    dp[i][j] = height[0][0]
                else:
                    dp[i][j] = min(height[i - 1][j - 1], max(dp[i - 1][j], dp[i][j - 1]))

        return dp[-1][-1]


class Solution2:


    def findMaxMin(self, matrix):
        global max_val
        global row
        global col

        row = len(matrix)
        col = len(matrix[0])
        min_val = sys.maxsize

        self.dfs(matrix, min_val, 0, 0)

        return max_val

    def dfs(self, matrix, min_val, i, j):
        global max_val
        global row
        global col

        if i >= row or j >= col:
            return
        if i == row - 1 and j == col -1:
            min_val = min(min_val, matrix[i][j])

            max_val = max(max_val, min_val)
            return

        min_val = min(min_val, matrix[i][j])
        self.dfs(matrix, min_val, i, j + 1)
        self.dfs(matrix, min_val, i + 1, j)



max_val = -sys.maxsize - 1
row = 0
col = 0






class Solution3:


    def findMaxMin(self, matrix):

        self.max_val = -sys.maxsize - 1
        self.row = len(matrix)
        self.col = len(matrix[0])
        min_val = sys.maxsize

        self.dfs(matrix, min_val, 0, 0)

        return self.max_val

    def dfs(self, matrix, min_val, i, j):


        if i >= self.row or j >= self.col:
            return
        if i == self.row - 1 and j == self.col -1:
            min_val = min(min_val, matrix[i][j])
            self.max_val = max(self.max_val, min_val)
            return

        min_val = min(min_val, matrix[i][j])
        self.dfs(matrix, min_val, i, j + 1)
        self.dfs(matrix, min_val, i + 1, j)









bb = Solution3()
result = bb.findMaxMin([[8, 4, 7],[6, 5, 9]])
print(result)





