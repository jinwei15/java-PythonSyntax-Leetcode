import java.util.HashMap;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class SingleNumber {

	/**
	 * @param args
	 *            Given a non-empty array of integers, every element appears twice
	 *            except for one. Find that single one.
	 * 
	 *            Note:
	 * 
	 *            Your algorithm should have a linear runtime complexity. Could you
	 *            implement it without using extra memory?
	 * 
	 *            Example 1:
	 * 
	 *            Input: [2,2,1] Output: 1 Example 2:
	 * 
	 *            Input: [4,1,2,1,2] Output: 4
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SingleNumberSolution {
	public int singleNumber(int[] nums) {

		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int i = 0; i < nums.length; i++) {
			if (!map.containsKey(nums[i])) {
				map.put(nums[i], 1);
			} else
				map.put(nums[i], map.get(nums[i]) + 1);
		}

		for (int num : nums) {
			if (map.get(num) == 1)
				return num;
		}
		return -1;

	}
}
