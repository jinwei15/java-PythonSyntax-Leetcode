/**
 * 
 */

/**
 * @author sgjzha34
 *
 */
public class ClimbingStairs {

	/**
	 * @param args
	 * 
	 *            You are climbing a stair case. It takes n steps to reach to the
	 *            top.
	 * 
	 *            Each time you can either climb 1 or 2 steps. In how many distinct
	 *            ways can you climb to the top?
	 * 
	 *            Note: Given n will be a positive integer.
	 * 
	 *            Example 1:
	 * 
	 *            Input: 2 Output: 2   
	 *            Explanation: There are two ways to climb to the
	 *            top. 
	 *            
	 *            1. 1 step + 1 step 
	 *            2. 2 steps 
	 *            
	 *            Example 2: Input: 3 Output: 3 
	 *            Explanation: There are three ways to climb to the top. 
	 *            1. 1 step + 1 step + 1 step 
	 *            2. 1 step + 2 steps 
	 *            3. 2 steps + 1 step
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionClimbingStairs bb =new SolutionClimbingStairs();
		
		System.out.println(bb.climbStairs(35));
	}

}

//https://blog.csdn.net/u011889952/article/details/44813593
class SolutionClimbingStairs {
    public int climbStairs(int n) {
    	double result = 0;
    	//C100,0+C99,1+C98,2+....+C50,50
    	for(int i = n ; i>=n/2; i--) {
    		//c 100 100-100
    		result = result + combination(i,n-i);
    		
    	}
    	
    	
		return (int)result;
        
    }
    
    /** 
     * factorial，n! = n * (n-1) * ... * 2 * 1 
     * @param n 
     * @return 
     */  
    private double factorial(int n) {  
        return (n > 1) ? n * factorial(n - 1) : 1;  
    }  
      
    /** 
     * arrangement A(n, m) = n!/(n-m)! 
     * @param n 
     * @param m 
     * @return 
     */  
    public double arrangement(int n, int m) {  
        return (n >= m) ? factorial(n) / factorial(n - m) : 0;  
    }  
    
    /** 
     * combination C(n, m) = n!/((n-m)! * m!) 
     * @param n 
     * @param m 
     * @return 
     */  
    public  double combination(int n, int m) {  
        return (n >= m) ? factorial(n) / (factorial(n - m) * factorial(m)) : 0;  
    } 
}


