/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class CardFlippingGame {

	/**
	 * @param args
	 *            On a table are N cards, with a positive integer printed on the
	 *            front and back of each card (possibly different).
	 * 
	 *            We flip any number of cards, and after we choose one card.
	 * 
	 *            If the number X on the back of the chosen card is not on the front
	 *            of any card, then this number X is good.
	 * 
	 *            What is the smallest number that is good? If no number is good,
	 *            output 0.
	 * 
	 *            Here, fronts[i] and backs[i] represent the number on the front and
	 *            back of card i.
	 * 
	 *            A flip swaps the front and back numbers, so the value on the front
	 *            is now on the back and vice versa.
	 * 
	 *            Example:
	 * 
	 *            Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3] Output: 2
	 *            Explanation: If we flip the second card, the fronts are
	 *            [1,3,4,4,7] and the backs are [1,2,4,1,3]. We choose the second
	 *            card, which has number 2 on the back, and it isn't on the front of
	 *            any card, so 2 is good.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionCardFlippingGame {
	public int flipgame(int[] fronts, int[] backs) {

		// int smallest = Integer.MAX_VALUE;
		// for (int i = 0; i < fronts.length; i++) {
		// if (fronts[i] != backs[i]) {
		// int temp = fronts[i];
		// fronts[i] = backs[i];
		// backs[i] = temp;
		//
		// boolean flag = true;
		// for (int j = 0; j < fronts.length; j++) {
		// if (fronts[j] == backs[i]) {
		// flag = false;
		//
		// }
		// }
		//
		// if (flag == true && smallest > backs[i]) {
		// smallest = backs[i];
		// }
		// }
		// }
		//
		// if(smallest> 2000) {
		// return 0;
		// }else {
		// return smallest;
		// }
		//

		int smallest = Integer.MAX_VALUE;
		for (int i = 0; i < fronts.length; i++) {
			if (backs[i] != fronts[i]) {
				boolean flag = true;
				int j = 0;
				while (j < backs.length && flag == true) {
					if (backs[j] == fronts[j] && fronts[j] == fronts[i]) {
						flag = false;
					}
					j++;

				}

				if (flag == true && fronts[i] < smallest) {
					smallest = fronts[i];
				}
			}
		}

		for (int i = 0; i < backs.length; i++) {
			if (backs[i] != fronts[i]) {
				boolean flag = true;
				int j = 0;
				while (j < fronts.length && flag == true) {
					if (backs[j] == fronts[j] && backs[j] == backs[i]) {
						flag = false;
					}
					j++;

				}

				if (flag == true && backs[i] < smallest) {
					smallest = backs[i];
				}
			}
		}

		if (smallest > 2000) {
			return 0;
		} else {
			return smallest;
		}

	}
}
