
/**
 * @author Jinwei Zhang
 * 
 *         Given an array of integers, return indices of the two numbers such
 *         that they add up to a specific target.
 * 
 *         You may assume that each input would have exactly one solution, and
 *         you may not use the same element twice.
 * 
 *         Example:
 * 
 *         Given nums = [2, 7, 11, 15], target = 9,
 * 
 *         Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
 */
public class TwoSum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class Solution {
	public int[] twoSum(int[] nums, int target) {
		int[] answer = new int[2];

		// loop through the array to check the index
		for (int i = 0; i < nums.length; i++) {
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[i] + nums[j] == target) {

					answer[0] = i;
					answer[1] = j;
				}

			}

		}
		return answer;
	}
}
