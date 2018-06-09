/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class TwoSumII_InputArraySorted {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class TwoSumII_InputArraySortedSolution {
	public int[] twoSum(int[] numbers, int target) {
		int left = 0;
		int right = numbers.length - 1;
		int[] ans = new int[2];
		boolean found = false;
		// find the answer then stop
		while (!found && numbers.length >= 2) {
			int temp = numbers[left] + numbers[right];
				if (temp == target) {
					ans[0] = left+1;
					ans[1] = right+1;
					found = true;
				} else if (temp > target) {
                    //decrease the number
					right--;
					
				}else {
					
					//increase
					left++;
				}
			

		}

		return ans;
	}
}
