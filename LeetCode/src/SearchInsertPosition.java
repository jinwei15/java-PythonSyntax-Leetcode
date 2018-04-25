/**
 * 
 */

/**
 * @author jinweizhang
 * 
 *         Given a sorted array and a target value, return the index if the
 *         target is found. If not, return the index where it would be if it
 *         were inserted in order.
 * 
 *         You may assume no duplicates in the array.
 * 
 *         Example 1:
 * 
 *         Input: [1,3,5,6], 5 Output: 2 Example 2:
 * 
 *         Input: [1,3,5,6], 2 Output: 1 Example 3:
 * 
 *         Input: [1,3,5,6], 7 Output: 4 Example 4:
 * 
 *         Input: [1,3,5,6], 0 Output: 0
 *
 */
public class SearchInsertPosition {

	/**
	 * @param args
	 * 
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionSearchInsertPosition {
	public int searchInsert(int[] nums, int target) {
		//
		// // boolean finishFlag = false;
		// int startIndex = 0;
		// int endIndex = nums.length - 1;
		// int middleIndex;
		// while (startIndex != endIndex) {
		// middleIndex = (startIndex + endIndex) / 2;
		// if (startIndex == middleIndex) {
		// if (nums[middleIndex] < target && nums[middleIndex + 1] >= target) {
		//
		// return middleIndex + 1;
		// } else if (nums[middleIndex] < target && nums[middleIndex + 1] < target) {
		// return middleIndex + 2;
		// } else {
		// return middleIndex;
		// }
		// } else {
		// if (nums[middleIndex] < target) {
		//
		// startIndex = middleIndex;
		//
		// } else if (nums[middleIndex] > target) {
		// // if (startIndex == middleIndex) {
		// // return middleIndex + 1;
		// // } else {
		// endIndex = middleIndex;
		// // }
		//
		// } else {
		// return middleIndex;
		// }
		// }
		//
		// }
		// if (target <= nums[startIndex]) {
		// return startIndex;
		// } else {
		// return startIndex+1;
		// }

		int start = 0, end = nums.length - 1;
		while (start < end) {
			int middle = (start + end) / 2;
			if (nums[middle] < target) {
				start = middle + 1;
			} else if (nums[middle] > target) {
				end = middle;
			} else
				return middle;
		}

		return target > nums[start] ? start + 1 : start;

	}
}
