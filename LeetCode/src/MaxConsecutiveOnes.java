
public class MaxConsecutiveOnes {
	public static void main(String[] args) {
		MaxConsecutiveOnesSolution bb = new MaxConsecutiveOnesSolution();

	}
}

class MaxConsecutiveOnesSolution {
	public int findMaxConsecutiveOnes(int[] nums) {
		int count = 0, result = 0;
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] == 1) {
				count++;
				result = Math.max(count, result);
			} else
				count = 0;
		}
		return result;
	}
}