import java.util.HashSet;
import java.util.Set;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class UniqueMorseCodeWords {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] words = { "gin", "zen", "gig", "msg" };
		Solution bb = new Solution();

		System.out.println(bb.uniqueMorseRepresentations(words));
	}

}

class Solution {
	public int uniqueMorseRepresentations(String[] words) {
		String[] MORSE = new String[] { ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
				".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
				"--.." };
		Set<String> set = new HashSet<String>();

		for (String word : words) {
			char[] list = word.toCharArray();
			StringBuilder code = new StringBuilder();
			for (char c : list) {
				code.append(MORSE[c - 'a']);
			}
			set.add(code.toString());
		}

		return set.size();
	}
}