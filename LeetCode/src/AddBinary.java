/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class AddBinary {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionAddBinary aa = new SolutionAddBinary();
		String a= "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
		String b="110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";

		System.out.println(aa.addBinary(a, b));
		
	}

}


class SolutionAddBinary {
	 public String addBinary(String a, String b) {
	        int lengthA = a.length();
	        int lengthB = b.length();
	        int[] result = new int[Math.max(lengthA, lengthB)+1];
	        int[] numsA = new int[lengthA], numsB = new int[lengthB];
	            //reverse
	        for(int i=0;i<lengthA;i++){
	            numsA[i] = a.charAt(numsA.length-1-i)-'0';
	        }
	        
	          for(int i=0;i<lengthB;i++){
	            numsB[i] = b.charAt(numsB.length-1-i)-'0';
	        }
	       
	 
	        for(int i =0;i<result.length-1;i++){
	          if(i<lengthA && i>=lengthB){
	              result[i] += numsA[i];
	          }else if(i>=lengthA && i<lengthB){
	              result[i] += numsB[i];
	          }else if(i<lengthA && i<lengthB){
	              result[i] += numsB[i];
	              result[i] += numsA[i];
	          }
	            if(result[i]==2||result[i]==3){
	                  result[i] = result[i]%2;
	                  result[i+1]++;
	              }
	            
	        }
	        
	        
	         final int RADIX = 10;
	        if(result[result.length-1]==0){
	            char strArray[] = new char[result.length-1];
	            for (int i = 0; i < result.length-1; i++)
			
	           

	strArray[i] = Character.forDigit(result[result.length-1-1-i], RADIX);
	            return  String.valueOf(strArray);
	        }else{
	            char strArray[] = new char[result.length];
	            for (int i = 0; i < result.length; i++)
				strArray[i] = Character.forDigit(result[result.length-1-i], RADIX);
	            return  String.valueOf(strArray);
	        }
	        	

			
	        
	        
	        
//	          long number0 = Long.parseLong(a, 2);
//	         long number1 = Long.parseLong(b, 2);

//	         return  Long.toBinaryString(number0 + number1); 
	      //string to int
	        
	        
//	         double numA = Double.parseDouble(a);	
//	         double numB = Double.parseDouble(b);
//	         double sum = numA+numB;
	        
//	         //int to string
//	         String temp = String.valueOf(sum);
//	         int[] digits = new int[temp.length()];
//	         for (int i = 0; i < temp.length(); i++)
//	         {
//	             digits[i] = temp.charAt(i) - '0';
//	         }
	        
	        
//	         for (int i = digits.length - 1; i >= 0; i--) {
//	 			if (digits[i] == 2 || digits[i] == 3) {
//	 				digits[i] = digits[i]%2;
//	 				//if the i is with in the bound
//	 				if (i - 1 >= 0) {
//	 					digits[i - 1]++;
//	 				} else {
//	 					//default as all 0
//	                   int []newArr = new int[digits.length+1];
//	                    newArr[0] = 1;
//	                     for(int j =0;j<digits.length;j++){
//	                         newArr[j+1] = digits[j];
//	                     }
//	                       digits = new int[digits.length+1];
//	                     digits = newArr;
//	 				}

//	 			}
//	 		}
	        
//	         return Arrays.toString(digits).replaceAll("\\[|\\]|,|\\s", "");
	        
	        
	    }
}