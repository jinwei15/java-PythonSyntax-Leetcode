import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class DiagonalTraverse {

	/**
	 * @param args
	 *            489 Given a matrix of M x N elements (M rows, N columns), return
	 *            all elements of the matrix in diagonal order as shown in the below
	 *            image.
	 * 
	 *            Example: Input: [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] Output:
	 *            [1,2,4,7,5,3,6,8,9] Explanation:
	 * 
	 *            Note: The total number of elements of the given matrix will not
	 *            exceed 10,000.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionDiagonalTraverse bb = new SolutionDiagonalTraverse();
		int[][] matrix = { {1,2,3},{1,2,3},{1,2,3},{1,2,3}};
		bb.findDiagonalOrder(matrix);
	}

}

class SolutionDiagonalTraverse {
	// on the top bottom border turn
	public int[] findDiagonalOrder(int[][] matrix) {
		int[] result = new int[0];
		int maxRow = matrix.length;
		//System.out.println(maxRow);
		if (maxRow == 0)
			return result;
		int maxColumn = matrix[0].length;
		if (maxRow == 1 && maxColumn == 0) {
			return result;
		} else {
			result = new int[maxRow * maxColumn];
		}

		int x = 0;
		int preX = 0;
		int preY = 0;
		int y = 0;
		result[0] = matrix[0][0];
		int currentIndex = 0;
		int[] rightDia = new int[2];
		int[] right = new int[2];
		int[] down = new int[2];
		int[] leftDia = new int[2];
		while (currentIndex < maxRow * maxColumn - 1) {
			right[0] = x;
			right[1] = y + 1;
			rightDia[0] = x - 1;
			rightDia[1] = y + 1;
			down[0] = x + 1;
			down[1] = y;
			leftDia[0] = x + 1;
			leftDia[1] = y - 1;

			// can you go diagonal? yes
			if (rightDia[1] < maxColumn && rightDia[0] * rightDia[1] >= 0
					&&(preX!=rightDia[0]||preY!=rightDia[1])) {
				// System.out.println(currentIndex);

				result[currentIndex + 1] = matrix[rightDia[0]][rightDia[1]];
				
				preX = x;
				preY = y;
				x = rightDia[0];
				y = rightDia[1];
				

			} else if (leftDia[0] < maxRow && leftDia[0] * leftDia[1] >= 0
					&&(preX!=leftDia[0]||preY!=leftDia[1])) {

				result[currentIndex + 1] = matrix[leftDia[0]][leftDia[1]];
				preX = x;
				preY = y;
				x = leftDia[0];
				y = leftDia[1];
			} else {
				// can not go diagonally Oops haha

				// can only go right
				if (right[0] * right[1] >= 0 && down[0] * down[1] < 0) {
					result[currentIndex + 1] = matrix[right[0]][right[1]];
					preX = x;
					preY = y;
					x = right[0];
					y = right[1];
					// can only go down
				} else if (right[0] * right[1] < 0 && down[0] * down[1] >= 0) {
					result[currentIndex + 1] = matrix[down[0]][down[1]];
					preX = x;
					preY = y;
					x = down[0];
					y = down[1];
					// can go both
				} else {
					// go right
					if ((x == 0 || x == maxRow - 1) && right[1] < maxColumn) {

						result[currentIndex + 1] = matrix[right[0]][right[1]];
						preX = x;
						preY = y;
						x = right[0];
						y = right[1];
					} else {
//						System.out.println(currentIndex + 1+" "+ down[0]+" "+down[1]);
//						System.out.println(x+" "+y+" "+ right[1]);
//						System.out.println();
						result[currentIndex + 1] = matrix[down[0]][down[1]];
						preX = x;
						preY = y;
						x = down[0];
						y = down[1];
					}
				}

			}
			currentIndex++;
			// System.out.println(x + "" + y + " ind:"+ currentIndex);
		}

		// for (int i = 0; i < maxRow*maxColumn; i++) {
		//
		// System.out.println(result[i]);
		//
		// }
		return result;
	}
}
