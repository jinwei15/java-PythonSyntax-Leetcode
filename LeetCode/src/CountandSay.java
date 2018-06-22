import java.util.ArrayList;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class CountandSay {

	/**
	 * @param args
	 *            The count-and-say sequence is the sequence of integers with the
	 *            first five terms as following:
	 * 
	 *            1. 1 2. 11 3. 21 4. 1211 5. 111221
	 * 
	 *            Note: Each term of the sequence of integers will be represented as
	 *            a string.
	 * 
	 *            Example 1:
	 * 
	 *            Input: 1 Output: "1" Example 2:
	 * 
	 *            Input: 4 Output: "1211"
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class Solution {
	public String countAndSay(int n) {
		if(n==1) return "1";
		if(n==2) return "11";

		ArrayList<Integer> previous = new ArrayList<Integer>();
		ArrayList<Integer> holding = new ArrayList<Integer>();
		String result = "";
		
		previous.add(1);
		previous.add(1);
		int pointer = 0;
		int amount = 0;
		for (int i=3; i<=n;i++) {
			while(pointer<previous.size()) {
				int currentNum = previous.get(pointer);
				pointer++;
				while(currentNum == previous.get(pointer)&&pointer<previous.size()) {
					amount++;
					
				}
				
			}
			
		}
		
		return result;
	}
}
