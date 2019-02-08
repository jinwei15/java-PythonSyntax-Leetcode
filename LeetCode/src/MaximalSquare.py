# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4
class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        # using dp easy to solve
        if matrix == None or len(matrix) == 0:
            return 0

        biggest = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])

                elif i > 0 and j > 0 and int(matrix[i][j]) != 0:
                    matrix[i][j] = min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1])) + 1

                if int(matrix[i][j]) > biggest:
                    biggest = matrix[i][j]

        return biggest * biggest





