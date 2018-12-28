import  sys
class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        iniHealth = 0
        row = len(dungeon)
        column = len(dungeon[0])
        optimal = [[-sys.maxsize-1 for i in range(column + 1)] for j in range(row + 1)]
        optimal[1][1] = dungeon[0][0]
        for i in range(1, row + 1):
            for j in range(1, column + 1):
                preMax = max(optimal[i - 1][j], optimal[i][j - 1])
                optimal[i][j] = dungeon[i - 1][j - 1] + preMax

        #                 if i == row  and j == column :
        #                     preMax = min(optimal[i - 1][j], optimal[i][j - 1])
        #                     optimal[i][j] = dungeon[i - 1][j - 1] + preMax
        # print(optimal)
        return optimal[-1][-1]

bb = Solution()
bb.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])

