#
# 2. MaximumMinimumPath (DFS)
#
# (一个小哥去爬山，给一个矩阵，要从左上角爬到右下角，每一步只能往右往下走。矩阵的每一个值是这一点的海拔。显然有很多条路可以走，每一条路都有一个经过的海拔最低值，求所有路径的海拔最低值的最大值。
# 比如：
# 5 4 5
# 1 3 6
# 有三条路可以走：5 1 3 6，5 4 3 6，5 4 5 6。三条路的最小值分别是1,3,4。求的就是这三个数的最大值，也就是4。我直接暴力写的。)
#
#
# ..给一个二维矩阵，表示某点的高度，人从左上角出发， 只能向下或向右走，最终到达右下角。
# 求所有可能的路径中每个路径最低点的最大值。
# 典型DP， 类似LC174
# 好像没在地里见过。
#
#
# ..maximum minimum path：直接二维dp做了，没啥特别奇怪的地方。。
#
#
# ..https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=457483&page=1#pid5030286
#
# ..Max min path from top left to bottom right.
# 基本的DP，开始用了个matrix存，后来有时间就优化了一下用个1D array存。肯定是最优了。
#
#
# ..另一道是miximin path, 经典的dp问题。两道题的Java代码都可以在小土刀上找到。
#
# ..2）maximum minimum path，可以参考这个帖子：http://www.1point3acres.com/bbs/thread-443128-1-1.html。我准备时正好没有写到这个题，
# 只好硬写，用了DFS遍历。我用python写的，然后看到IDE里提供的API没有定义class
# （不是像利扣的那样有定义个 class Solution(object)），
# 所以没法用def __init__(self)来定义 self.maximum 这个变量（因为需要不断更新）。
# 我后来有些急，就用了一个minimumValueList 来存每条路径的最小值，最后返回 max(minimumValueList)。但这样的复杂度其实很高，后来OA结束后，我重写了一遍，用 global maximum 就可以了。
# 总结来说，还是自己对 global 的使用不太熟。
#


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

