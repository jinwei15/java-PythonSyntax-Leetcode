import java.util.*;

import javax.print.attribute.standard.RequestingUserName;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class NextGreaterElementI {

	/**
	 * @param args
	 *            You are given two arrays (without duplicates) nums1 and nums2
	 *            where nums1’s elements are subset of nums2. Find all the next
	 *            greater numbers for nums1's elements in the corresponding places
	 *            of nums2.
	 * 
	 *            The Next Greater Number of a number x in nums1 is the first
	 *            greater number to its right in nums2. If it does not exist, output
	 *            -1 for this number.
	 * 
	 *            Example 1: Input: nums1 = [4,1,2], nums2 = [1,3,4,2]. Output:
	 *            [-1,3,-1] Explanation: For number 4 in the first array, you cannot
	 *            find the next greater number for it in the second array, so output
	 *            -1. For number 1 in the first array, the next greater number for
	 *            it in the second array is 3. For number 2 in the first array,
	 *            there is no next greater number for it in the second array, so
	 *            output -1.
	 * 
	 *            Example 2: Input: nums1 = [2,4], nums2 = [1,2,3,4]. Output: [3,-1]
	 * 
	 *            Explanation: For number 2 in the first array, the next greater
	 *            number for it in the second array is 3. For number 4 in the first
	 *            array, there is no next greater number for it in the second array,
	 *            so output -1.
	 * 
	 *            Note: All elements in nums1 and nums2 are unique. The length of
	 *            both nums1 and nums2 would not exceed 1000.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution solution = new Solution();
		int[] result = solution.nextGreaterElement(new int[] { 4, 1, 2 }, new int[] { 1, 3, 4, 2 });
		System.out.println(Arrays.toString(result));
	}

}

//class Solution {
//	public int[] nextGreaterElement(int[] nums1, int[] nums2) {
//		//misunderstanding
//		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
//
//		for (int i = 0; i < nums2.length; i++) {
//			if (i == nums2.length - 1) {
//				map.put(nums2[i], -1);
//			} else {
//				map.put(nums2[i], nums2[i + 1]);
//			}
//		}
//
//		for (int i = 0; i < nums1.length; i++) {
//			int value = map.get(nums1[i]);
//			if (value > nums1[i]) {
//				nums1[i] = value;
//			}else {
//				nums1[i] = -1;
//			}
//		}
//
//		return nums1;
//
//	}
//}

class Solution {
	 public int[] nextGreaterElement(int[] findNums, int[] nums) {
       Map<Integer, Integer> map = new HashMap<>(); // map from x to next greater element of x
       Stack<Integer> stack = new Stack<>();
       for (int num : nums) {
           while (!stack.isEmpty() && stack.peek() < num)
               map.put(stack.pop(), num);
           stack.push(num);
       }   
       for (int i = 0; i < findNums.length; i++)
           findNums[i] = map.getOrDefault(findNums[i], -1);
       return findNums;
   }
}


