import java.util.ArrayList;
import java.util.List;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class SpiralMatrix {

	/**
	 * @param args
	 *            Given a matrix of m x n elements (m rows, n columns), return all
	 *            elements of the matrix in spiral order.
	 * 
	 *            Example 1:
	 * 
	 *            Input: [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] Output:
	 *            [1,2,3,6,9,8,7,4,5] Example 2:
	 * 
	 *            Input: [ [1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12] ] Output:
	 *            [1,2,3,4,8,12,11,10,9,5,6,7]
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class SolutionSpiralMatrix {
	 public List<Integer> spiralOrder(int[][] matrix) {
	       
	        int [][] dir = new int[][] {{0,1},{1,0},{0,-1},{-1,0}};
	        List <Integer> result = new ArrayList<Integer>();
	       if (matrix == null || matrix.length == 0) return result;
	        //right down left up
	        int[] Border = new int[]{matrix[0].length,matrix.length,-1,0};

	        int[] location = new int[]{0,0};
	        int index = 0;
	        //result.add(matrix[location[0]][location[1]]);
	        for(int i = 0; i< matrix.length*matrix[0].length;i++){
	            
	            
	            result.add(matrix[location[0]][location[1]]);
	            int tempX = location[0] + dir[index][0];
	            int tempY = location[1] + dir[index][1];;
	            if((index==0 && tempY >= Border[index])|| (index==1 && tempX >= Border[index])){
	             
	                    Border[index]--;
	                    index++;

	                 
	             }else if( (index == 2 && tempY<=Border[index])|| (index == 3 && tempX<=Border[index])){
	                    Border[index]++;
	                    index++;
	            }
	          
	            index = index%4;
	            location[0]+=dir[index][0];
	            location[1]+=dir[index][1];
	            
	      
	            
	        }
	        
	        
	        return result;
	    }
}
