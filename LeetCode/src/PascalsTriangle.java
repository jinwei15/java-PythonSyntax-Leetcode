import java.util.ArrayList;
import java.util.List;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class PascalsTriangle {

	/**
	 * @param args
	 *            Given a non-negative integer numRows, generate the first numRows
	 *            of Pascal's triangle.
	 * 
	 * 
	 *            In Pascal's triangle, each number is the sum of the two numbers
	 *            directly above it. Example:
	 * 
	 *            Input: 5 Output: [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionPascalsTriangle bb =new SolutionPascalsTriangle();
		bb.generate(5);
	}

}

class SolutionPascalsTriangle {
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		List<Integer> first = new ArrayList<Integer>();
		first.add(1);
		result.add(first);
		List<Integer> second = new ArrayList<Integer>();
		second.add(1);
		second.add(1);
		result.add(second);

		for (int i = 2; i < numRows; i++) {
			List<Integer> more = new ArrayList<Integer>();
			for (int j = 0; j < i; j++) {
				
				if (j == 0 || j == i - 1) {
					more.add(1);
				} else {
					//System.out.println(i+" "+j);
					more.add(result.get(i - 1).get(j - 1) + result.get(i - 1).get(j));
				}

				
			}
			result.add(more);
		}
		return result;

	}
}
