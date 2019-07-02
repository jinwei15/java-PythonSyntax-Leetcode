import copy
from typing import *

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copyBoard = copy.deepcopy(board)
        rows = len(board)
        cols = len(board[0])
        # copyBoard = [[board[row][col] for col in range(cols)] for row in range(rows)]
        for i in range(rows):
            for j in range(cols):
                live, dead = self.countLife(i, j, copyBoard)
                # print(i,j,"->" ,live ,dead)
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 1
                elif board[i][j] == 1 and live < 2:
                    board[i][j] = 0
                elif board[i][j] == 1 and live > 3:
                    board[i][j] = 0

    def countLife(self, x, y, board):
        live, dead = 0, 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i != x or j != y):
                    if board[i][j] == 0:
                        dead += 1
                    else:
                        live += 1
        return live, dead


