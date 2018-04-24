import java.util.HashSet;
import java.util.Set;

public class RemoveDuplicatesFromSortedArray {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionRemoveDuplicatesFromSortedArray dd = new SolutionRemoveDuplicatesFromSortedArray();
		int[] arr = new int[] {1,2,3,4};
		dd.removeDuplicates(arr);
	}
}

class SolutionRemoveDuplicatesFromSortedArray {
	//this is the first try of the solution
	public int removeDuplicates(int[] nums) {
	int end = nums.length;
	Set<Integer> set = new HashSet<Integer>();

	for(int i = 0; i < end; i++){
	set.add(nums[i]);
	}


	int[] y = new int[set.size()];
	int c = 0;
	for(int x : set) y[c++] = x;

	return set.size();
	}

//this is the standard solution 
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

		for (int j = 0; j < nums.length; j++) {
			System.out.print(nums[j]);
		}

		return i + 1;
	}
}
