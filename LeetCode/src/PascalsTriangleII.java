import java.util.ArrayList;
import java.util.List;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class PascalsTriangleII {

	/**
	 * @param args
	 *            Given a non-negative index k where k ≤ 33, return the kth index
	 *            row of the Pascal's triangle.
	 * 
	 *            Note that the row index starts from 0.
	 * 
	 * 
	 *            In Pascal's triangle, each number is the sum of the two numbers
	 *            directly above it.
	 * 
	 *            Example:
	 * 
	 *            Input: 3 Output: [1,3,3,1]
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionPascalsTriangleII {
	public List<Integer> getRow(int rowIndex) {

		List<List<Integer>> result = new ArrayList<List<Integer>>();
		
		List<Integer> first = new ArrayList<Integer>();
		first.add(1);
		result.add(first);
		
		if (rowIndex == 0)
			return result.get(0);
		
		List<Integer> second = new ArrayList<Integer>();
		second.add(1);
		second.add(1);
		result.add(second);
		
		if (rowIndex == 1)
			return result.get(1);

		for (int i = 2; i <= rowIndex; i++) {
			List<Integer> more = new ArrayList<Integer>();
			for (int j = 0; j <= i; j++) {

				if (j == 0 || j == i) {
					more.add(1);
				} else {
					// System.out.println(i+" "+j);
					more.add(result.get(i - 1).get(j - 1) + result.get(i - 1).get(j));
				}

			}
			result.add(more);
		}
		return result.get(rowIndex);

	}

}