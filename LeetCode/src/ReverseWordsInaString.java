/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class ReverseWordsInAString {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseWordsInAStringSolution tryOne  = new ReverseWordsInAStringSolution();
		String result = tryOne.reverseWords(" ");
		System.out.println("result is:"+ result);
	}

}


class ReverseWordsInAStringSolution {
    public String reverseWords(String s) {

    	//cut the string to the sub string if there is any space in the front or the end 
    	 if (s.length() == 0) {
 		   return "";
    	 }
    	 
    	 boolean found = false;
    	 int startIndex = 0;
    	 int endIndex = s.length()-1;
    	 while(!found&&startIndex<=endIndex) {
    		 if(s.charAt(startIndex)!=' '&&s.charAt(endIndex)!=' ') found = true;
    		 
    		 if(s.charAt(startIndex)==' ') startIndex ++;
    		 
    		 if(s.charAt(endIndex)==' ') endIndex --;
    		 
    	 }
if(startIndex<=endIndex) {
	s = s.substring(startIndex, endIndex+1);
}else {
	return "";
}
    	 
// 	   }else if(s.charAt(0)== ' ') {
// 		  s = s.substring(1);
//    	   }else if (s.charAt(s.length()-1) == ' ') {
//    		   s = s.substring(0, s.length()-1);
//    	   }
        
        String[] splitStr = s.split("\\s+");
        String temp = null;
        
        if(splitStr.length == 1) return s.replaceAll("\\s+","");
        
        for (int i = 0 ; i<splitStr.length/2;i++){
            temp = splitStr[i];
            splitStr[i] = splitStr[splitStr.length-1-i];
            splitStr[splitStr.length-1-i] = temp;
                
        }
        
        String joined = String.join(" ", splitStr);
        return joined;
    }
}
