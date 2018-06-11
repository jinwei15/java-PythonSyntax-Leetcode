import java.util.HashMap;
import java.util.HashSet;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class IntersectionofTwoArrays {

	/**
	 * @param args
	 *            Given two arrays, write a function to compute their intersection.
	 * 
	 *            Example: Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
	 * 
	 *            Note: Each element in the result must be unique. The result can be
	 *            in any order.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class IntersectionofTwoArraysSolution {
	public int[] intersection(int[] nums1, int[] nums2) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		HashSet<Integer> result = new HashSet<Integer>();

		for (int i = 0; i < nums1.length; i++) {
			map.put(i, nums1[i]);
		}

		// see if the previous map contains the value if so add in the array list
		for (int i = 0; i < nums2.length; i++) {
			if (map.containsValue(nums2[i])) {
				result.add(nums2[i]);
			}
		}

		int[] ret = new int[result.size()];
		int i = 0;
		for (int a : result) {

			ret[i] = a;
			i++;
		}
		return ret;

	}
}
