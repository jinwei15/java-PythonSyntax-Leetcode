/**
 * 
 */

/**
 * @author jinweizhang Given an integer array nums, find the contiguous subarray
 *         (containing at least one number) which has the largest sum and return
 *         its sum.
 * 
 *         Example:
 * 
 *         Input: [-2,1,-3,4,-1,2,1,-5,4], Output: 6 Explanation: [4,-1,2,1] has
 *         the largest sum = 6. Follow up:
 * 
 *         If you have figured out the O(n) solution, try coding another
 *         solution using the divide and conquer approach, which is more subtle.
 *
 * 
 * 
 */
public class MaximumSubarray {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionMaximumSubarray {
	public int maxSubArray(int[] nums) {
		if (nums.length == 1)
			return nums[0];
		int sum = nums[0];
		int subSum = 0;
		for (int i = 0; i < nums.length; i++) {
			subSum = nums[i];
			if (subSum > sum) {
				sum = subSum;
			}
			for (int j = i + 1; j < nums.length; j++) {

				subSum = subSum + nums[j];

				if (subSum > sum) {
					sum = subSum;
				}
			}
		}
		return sum;
	}
}
