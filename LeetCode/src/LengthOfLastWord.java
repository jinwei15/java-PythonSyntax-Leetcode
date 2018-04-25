/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class LengthOfLastWord {

	/**
	 * @param args
	 * 
	 *            Given a string s consists of upper/lower-case alphabets and empty
	 *            space characters ' ', return the length of last word in the
	 *            string.
	 * 
	 *            If the last word does not exist, return 0.
	 * 
	 *            Note: A word is defined as a character sequence consists of
	 *            non-space characters only.
	 * 
	 *            Example:
	 * 
	 *            Input: "Hello World" Output: 5
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionLengthOfLastWord {
	public int lengthOfLastWord(String s) {
		String[] outcome = s.split(" ");
		return outcome.length > 0 ? outcome[outcome.length - 1].length() : 0;

	}
}
