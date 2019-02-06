class TicTacToe:

    def __init__(self, n: 'int'):
        """
        Initialize your data structure here.
        """
        self.allCol = [0 for _ in range(n)]
        self.allrow = [0 for _ in range(n)]
        self.n = n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: 'int', col: 'int', player: 'int') -> 'int':
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            toAdd = 1
        else:
            toAdd = -1

        self.allrow[row] += toAdd
        self.allCol[col] += toAdd

        if row == col:
            self.diagonal += toAdd
        if row + col + 1 == self.n:
            self.antiDiagonal += toAdd
        if abs(self.allrow[row]) == self.n or abs(self.allCol[col]) == self.n or abs(self.diagonal) == self.n or abs(self.antiDiagonal) == self.n:
            return player
        return 0
            
        
            


# # Your TicTacToe object will be instantiated and called as such:
# # obj = TicTacToe(n)
# # param_1 = obj.move(row,col,player)

# public class TicTacToe {
# private int[] rows;
# private int[] cols;
# private int diagonal;
# private int antiDiagonal;

# /** Initialize your data structure here. */
# public TicTacToe(int n) {
#     rows = new int[n];
#     cols = new int[n];
# }

# /** Player {player} makes a move at ({row}, {col}).
#     @param row The row of the board.
#     @param col The column of the board.
#     @param player The player, can be either 1 or 2.
#     @return The current winning condition, can be either:
#             0: No one wins.
#             1: Player 1 wins.
#             2: Player 2 wins. */
# public int move(int row, int col, int player) {
#     int toAdd = player == 1 ? 1 : -1;
    
#     rows[row] += toAdd;
#     cols[col] += toAdd;
#     if (row == col)
#     {
#         diagonal += toAdd;
#     }
    
#     if (col == (cols.length - row - 1))
#     {
#         antiDiagonal += toAdd;
#     }
    
#     int size = rows.length;
#     if (Math.abs(rows[row]) == size ||
#         Math.abs(cols[col]) == size ||
#         Math.abs(diagonal) == size  ||
#         Math.abs(antiDiagonal) == size)
#     {
#         return player;
#     }
    
#     return 0;
# }
# }
