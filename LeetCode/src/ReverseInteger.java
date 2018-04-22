import java.util.Scanner;

/**
 * 
 */

/**
 * @author jinweizhang
 * 
 *         Given a 32-bit signed integer, reverse digits of an integer.
 * 
 *         Example 1:
 * 
 *         Input: 123 Output: 321 Example 2:
 * 
 *         Input: -123 Output: -321 Example 3:
 * 
 *         Input: 120 Output: 21 Note: Assume we are dealing with an environment
 *         which could only store integers within the 32-bit signed integer
 *         range: [−231, 231 − 1]. For the purpose of this problem, assume that
 *         your function returns 0 when the reversed integer overflows.
 */
public class ReverseInteger {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int i = sc.nextInt();
		
		SolutionReverseInteger sd = new SolutionReverseInteger();
		int result = sd.reverse(i);
		System.out.print(result);
		
		sc.close();
	}

}

/*
 * Java reverse an int value - Principles
 * 
 * Modding (%) the input int by 10 will extract off the rightmost digit.
 * example: (1234 % 10) = 4 Multiplying an integer by 10 will "push it left"
 * exposing a zero to the right of that number, example: (5 * 10) = 50 Dividing
 * an integer by 10 will remove the rightmost digit. (75 / 10) = 7 Java reverse
 * an int value - Pseudocode:
 * 
 * a. Extract off the rightmost digit of your input number. (1234 % 10) = 4
 * 
 * b. Take that digit (4) and add it into a new reversedNum.
 * 
 * c. Multiply reversedNum by 10 (4 * 10) = 40, this exposes a zero to the right
 * of your (4).
 * 
 * d. Divide the input by 10, (removing the rightmost digit). (1234 / 10) = 123
 * 
 * e. Repeat at step a with 123
 * 
 * Java reverse an int value - Working code
 */
class SolutionReverseInteger {
	public int reverse(int x) {

		int reversedNum = 0;
		int input_long = x;
		if (reversedNum > Integer.MAX_VALUE || reversedNum < Integer.MIN_VALUE) {
			return 0;
		}else {
			while (input_long != 0) {
				reversedNum = reversedNum * 10 + input_long % 10;
				input_long = input_long / 10;
			}
		}
	

            return reversedNum;
		

	}
}
