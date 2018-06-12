public class Solution {
    public String reverseWords(String s) {

        
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
