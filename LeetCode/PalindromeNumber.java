/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class PalindromeNumber {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionPa pa = new SolutionPa();
		// print out the outcome
		System.out.println(pa.isPalindrome(121));

	}

}

class SolutionPa {
	public boolean isPalindrome(int x) {
		int palindrome = x;
		int reverse = 0;

		// Compute the reverse
		while (palindrome != 0) {
			int remainder = palindrome % 10;
			reverse = reverse * 10 + remainder;
			palindrome = palindrome / 10;
		}

		// The integer is palindrome if integer and reverse are equal

		if (x < 0) {
			return false;
		} else {
			return x == reverse; // Improved by Peter Lawrey
		}

	}

	// public boolean isPalindrome(int integer) {
	// String intStr = String.valueOf(integer);
	// return intStr.equals(new StringBuilder(intStr).reverse().toString());
	// }
}