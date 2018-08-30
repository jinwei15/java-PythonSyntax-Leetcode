/**
 * 
 */

/**
 * @author jinweizhang On a N * N grid, we place some 1 * 1 * 1 cubes that are
 *         axis-aligned with the x, y, and z axes.
 * 
 *         Each value v = grid[i][j] represents a tower of v cubes placed on top
 *         of grid cell (i, j).
 * 
 *         Now we view the projection of these cubes onto the xy, yz, and zx
 *         planes.
 * 
 *         A projection is like a shadow, that maps our 3 dimensional figure to
 *         a 2 dimensional plane.
 * 
 *         Here, we are viewing the "shadow" when looking at the cubes from the
 *         top, the front, and the side.
 * 
 *         Return the total area of all three projections.
 *
 */
public class ProjectionAreaof3DShapes {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class Solution {
	public int projectionArea(int[][] grid) {
		int ans = 0;
		// Retrieve all the element in the 2D array
		for (int i = 0; i < grid[0].length; i++) {
			int  row = 0, col = 0;
			for (int j = 0; j < grid[0].length; j++) {
				// add the x-y pane
				if (grid[i][j] > 0) {
					ans++;
				}

				row = Math.max(row, grid[i][j]);
				col = Math.max(col, grid[j][i]);
			}
			ans += row + col;
		}
		return ans;
	}
}
