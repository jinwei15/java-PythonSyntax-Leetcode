import java.util.HashSet;
import java.util.Set;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class ContainsDuplicate {

	/**
	 * @param args
	 *            Given an array of integers, find if the array contains any
	 *            duplicates.
	 * 
	 *            Your function should return true if any value appears at least
	 *            twice in the array, and it should return false if every element is
	 *            distinct.
	 * 
	 *            Example 1:
	 * 
	 *            Input: [1,2,3,1] Output: true Example 2:
	 * 
	 *            Input: [1,2,3,4] Output: false Example 3:
	 * 
	 *            Input: [1,1,1,3,3,4,3,2,4,2] Output: true
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class ContainsDuplicateSolution {
    public boolean containsDuplicate(int[] nums) {
         // Replace Type with actual type of your key
        HashSet<Integer> hashset = new HashSet<>();
        for (Integer key : nums) {
            if (hashset.contains(key)) {
                return true;
            }
            hashset.add(key);
        }
        return false;
    }
}
