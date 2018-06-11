import java.util.ArrayList;
import java.util.FormatFlagsConversionMismatchException;
import java.util.HashMap;

import javax.print.attribute.standard.RequestingUserName;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class HappyNumber {

	/**
	 * @param args
	 *            Write an algorithm to determine if a number is "happy".
	 * 
	 *            A happy number is a number defined by the following process:
	 *            Starting with any positive integer, replace the number by the sum
	 *            of the squares of its digits, and repeat the process until the
	 *            number equals 1 (where it will stay), or it loops endlessly in a
	 *            cycle which does not include 1. Those numbers for which this
	 *            process ends in 1 are happy numbers.
	 * 
	 *            Example:
	 * 
	 *            Input: 19 Output: true Explanation: 12 + 92 = 82 82 + 22 = 68 62 +
	 *            82 = 100 12 + 02 + 02 = 1
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class HappyNumberSolution {
	public boolean isHappy(int n) {
		HashMap<Integer, Integer> previous = new HashMap<Integer, Integer>();
		ArrayList<Integer> onHold = new ArrayList<Integer>();
		int total = 0;
		boolean moving = true;
        boolean result = false;
		while (moving) {
			while (n > 0) {
				onHold.add(n % 10);
				n = n / 10;
			}

			for (int i = 0; i < onHold.size(); i++) {
				total += Math.pow(onHold.get(i), 2);
			}
			// if found happy
			if (total == 1) {
				moving = false;
				result = true;
			} else {
				if (previous.containsKey(total)) {
					moving = false;
					result = false;
				} else {
					previous.put(total, 1);
				}
			}

		}
		
		return result;

	}
}
