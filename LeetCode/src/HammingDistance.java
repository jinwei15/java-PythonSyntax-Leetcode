/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class HammingDistance {

	/**
	 * @param args
	 *            The Hamming distance between two integers is the number of
	 *            positions at which the corresponding bits are different.
	 * 
	 *            Given two integers x and y, calculate the Hamming distance.
	 * 
	 *            Note: 0 ≤ x, y < 231.
	 * 
	 *            Example:
	 * 
	 *            Input: x = 1, y = 4
	 * 
	 *            Output: 2
	 * 
	 *            Explanation: 1 (0 0 0 1) 4 (0 1 0 0) ↑ ↑
	 * 
	 *            The above arrows point to positions where the corresponding bits
	 *            are different.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution bb = new Solution();
		int dis = bb.hammingDistance(4, 14);
		System.out.println(dis);
	}

}

class Solution {
	public int hammingDistance(int x, int y) {
		String bitX = Integer.toBinaryString(x);
		String bitY = Integer.toBinaryString(y);
		StringBuilder sbX = new StringBuilder( bitX);
		StringBuilder sbY = new StringBuilder( bitY);
		int length = bitX.length()-bitY.length();
		int distance = 0;
		if(length>0) {
			for(int i = 0; i<length; i++) {
				sbY.insert(0, '0');
			}
		}else if(length<0) {
			for(int i = 0; i<-length; i++) {
				sbX.insert(0, '0');
			}
		}
		for(int i = 0; i<sbX.length(); i++) {
			if(sbX.charAt(i) != sbY.charAt(i)) {
				distance ++;
			}
		}
		
		return distance;
	}
}

//return Integer.bitCount(x ^ y);
