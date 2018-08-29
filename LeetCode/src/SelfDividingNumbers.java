import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Currency;
import java.util.List;

import org.omg.CORBA.Current;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class SelfDividingNumbers {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution bb = new Solution();
		List result = bb.selfDividingNumbers(1, 22);
		System.out.println(result);
	}

}

class Solution {
	public List<Integer> selfDividingNumbers(int left, int right) {
		// create a new result list
		List<Integer> resultList = new ArrayList<Integer>();
		for (int i = left; i <= right; i++) {
			int currentNum = i;
			// convert the number to char array
			char[] currentChar = String.valueOf(currentNum).toCharArray();

			boolean flag = true;
			for (char l : currentChar) {
				if (l == '0' || currentNum % (l - '0') != 0) {
					flag = false;
					break;
				}
			}

			if (flag) {
				resultList.add(currentNum);
			}
		}
		return resultList;
	}
}
