/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class PlusOne {

	/**
	 * @param args
	 * 
	 *            Given a non-empty array of digits representing a non-negative
	 *            integer, plus one to the integer.
	 * 
	 *            The digits are stored such that the most significant digit is at
	 *            the head of the list, and each element in the array contain a
	 *            single digit.
	 * 
	 *            You may assume the integer does not contain any leading zero,
	 *            except the number 0 itself.
	 * 
	 *            Example 1:
	 * 
	 *            Input: [1,2,3] Output: [1,2,4] Explanation: The array represents
	 *            the integer 123. Example 2:
	 * 
	 *            Input: [4,3,2,1] Output: [4,3,2,2] Explanation: The array
	 *            represents the integer 4321.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionPlusOne {
	// [9,9,9] ???
	// [9] ??
	// [0]?
	public int[] plusOne(int[] digits) {
		int[] result = digits;
		result[result.length - 1]++;

		for (int i = digits.length - 1; i >= 0; i--) {
			if (result[i] == 10) {
				result[i] = 0;
				//if the i is with in the bound
				if (i - 1 >= 0) {
					result[i - 1]++;
				} else {
					//default as all 0
                   result = new int[digits.length+1];
                   result[0] = 1;
				}

			}
		}

		return result;
	}
}
