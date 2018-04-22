import java.util.HashSet;
import java.util.Set;

public class RemoveDuplicatesFromSortedArray {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}

class SolutionRemoveDuplicatesFromSortedArray {
	// public int removeDuplicates(int[] nums) {
	// int end = nums.length;
	// Set<Integer> set = new HashSet<Integer>();
	//
	// for(int i = 0; i < end; i++){
	// set.add(nums[i]);
	// }
	//
	//
	// int[] y = new int[set.size()];
	// int c = 0;
	// for(int x : set) y[c++] = x;
	//
	// return set.size();
	// }

	public int removeDuplicates(int[] nums) {
		if (nums.length == 0)
			return 0;
		int i = 0;
		for (int j = 1; j < nums.length; j++) {
			if (nums[j] != nums[i]) {
				i++;
				nums[i] = nums[j];
			}
		}
		return i + 1;
	}
}


//you know some time you think you are good.
//that is the time that you are being a fool;
//some time you are frustreted that is the time you are
//growing up. Hopefully you can learn form what you have
//missed and learn from it



//what have already passed can not go back. What you need to do
//is right now!.
