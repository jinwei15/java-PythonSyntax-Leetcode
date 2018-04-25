/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class ImplementStrStr {

	/**
	 * @param args
	 * 
	 *            Implement strStr().
	 * 
	 *            Return the index of the first occurrence of needle in haystack, or
	 *            -1 if needle is not part of haystack.
	 * 
	 *            Example 1:
	 * 
	 *            Input: haystack = "hello", needle = "ll" Output: 2 Example 2:
	 * 
	 *            Input: haystack = "aaaaa", needle = "bba" Output: -1
	 *            Clarification:
	 * 
	 *            What should we return when needle is an empty string? This is a
	 *            great question to ask during an interview.
	 * 
	 *            For the purpose of this problem, we will return 0 when needle is
	 *            an empty string. This is consistent to C's strstr() and Java's
	 *            indexOf().
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String haystack = "hello";
		String needle = "llo";

		int aa = haystack.indexOf(needle);
		System.out.println(aa);
	}

}

// easy solution git hub !!!!
class SolutionImplementStrStr {
	public int strStr(String haystack, String needle) {

		if (needle.isEmpty())
			return 0;
		for (int i = 0; i <= haystack.length() - needle.length(); i++) {
			if (haystack.substring(i, i + needle.length()).equals(needle))
				return i;
		}
		return -1;

	}
}
