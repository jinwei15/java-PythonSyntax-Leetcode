/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class ShortestDistancetoaCharacter {

	/**
	 * @param args
	 *            Given a string S and a character C, return an array of integers
	 *            representing the shortest distance from the character C in the
	 *            string.
	 * 
	 *            Example 1:
	 * 
	 *            Input: S = "loveleetcode", C = 'e' Output: [3, 2, 1, 0, 1, 0, 0,
	 *            1, 2, 2, 1, 0]
	 * 
	 * 
	 *            Note:
	 * 
	 *            S string length is in [1, 10000]. C is a single character, and
	 *            guaranteed to be in string S. All letters in S and C are
	 *            lowercase.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
//loveleetcode
		SolutionShortestDistancetoaCharacter bb =new SolutionShortestDistancetoaCharacter();
		
		for(int i =0;i<12;i++) {
			
			System.out.print(bb.shortestToChar("loveleetcode", 'e')[i]);
		}
	}

}

class SolutionShortestDistancetoaCharacter {
	public int[] shortestToChar(String S, char C) {
		int[] returnArr = new int[S.length()];

		for (int i = 0; i < S.length(); i++) {
			if (S.charAt(i) == C) {
				returnArr[i] = 0;
			}
		}
		for (int i = 0; i < S.length(); i++) {
			if (S.charAt(i) != C) {
				int reachLeft = i;
				int reachRight = i;
				boolean find = false;
				while (!find) {
					reachLeft--;
					reachRight++;
					if (reachLeft >= 0 && S.charAt(reachLeft) == C) {
						find = true;
						returnArr[i] = i-reachLeft;
					} else if (reachRight < S.length() - i && S.charAt(reachRight) == C) {
						find = true;
						returnArr[i] = reachRight-i;

					}

				}
			}
		}
		return returnArr;
	}
}
