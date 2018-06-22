class MinimumPathSumSolution {
     public int minPathSum(int[][] grid) {
         //rows
        final int m = grid.length;
         //column
        final int n = grid[0].length;
        if (m == 0) return 0;

        int[][] f = new int[m][n];
        f[0][0] = grid[0][0];
         
         //get the min column right
        for (int i = 1; i < m; i++) {
            f[i][0] = f[i - 1][0] + grid[i][0];
        }
         //get the row right for
        for (int i = 1; i < n; i++) {
            f[0][i] = f[0][i - 1] + grid[0][i];
        }

         //dynamic programming the array
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                f[i][j] = Math.min(f[i - 1][j], f[i][j - 1]) + grid[i][j];
            }
        }
         
         //return the last number
        return f[m - 1][n - 1];
    }
}
