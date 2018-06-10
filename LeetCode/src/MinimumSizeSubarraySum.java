/**
 * 
 */

/**
 * @author Jinwei Zhang
 *
 */
public class MinimumSizeSubarraySum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MinimumSizeSubarraySumSolution bb =new MinimumSizeSubarraySumSolution();
		bb.minSubArrayLen(11, new int[] {1,2,3,4,5});
	}

}

class MinimumSizeSubarraySumSolution {
	  public int minSubArrayLen(int s, int[] nums) {
        int min = 0;
        int result = Integer.MAX_VALUE;
        int sum = 0;
        if(nums.length==0) return 0;
        for (int i = 0;i<nums.length-1;i++){
            if(nums[i]<s){
                min = 1;
            }else{
                min = 0;
            }
            
            sum = nums[i];
            int j=i+1;
            while(j<nums.length){
                sum +=  nums[j];
             
                min ++;
                if (sum > s){
                    if(min < result){
                        result = min;
                    }
                    break;
                }
                j++;
            }
        }
        
        return result;
    }
}
}
