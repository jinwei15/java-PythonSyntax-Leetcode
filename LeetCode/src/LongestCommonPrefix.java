
public class LongestCommonPrefix {
	/**
	 * @param args
	 * 
	 *            Write a function to find the longest common prefix string amongst
	 *            an array of strings.
	 * 
	 *            If there is no common prefix, return an empty string "".
	 * 
	 *            Example 1:
	 * 
	 *            Input: ["flower","flow","flight"] Output: "fl"
	 * 
	 *            Example 2:
	 * 
	 *            Input: ["dog","racecar","car"] Output: ""
	 * 
	 *            Explanation: There is no common prefix among the input strings.
	 *            Note:
	 * 
	 *            All given inputs are in lower case letters a-z
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionLong bb =new SolutionLong();
		bb.longestCommonPrefix(new String[] {"aa","ab"});
		
  
	}

}

//this is the 
class SolutionLong {
	public String longestCommonPrefix(String[] strs) {
		int index = 0;
		String common = "";
		boolean hasFound = false;
		char pivot;

		// need to check pre-condition
		if (strs.length == 0 || strs[0].equals("")) {
			return "";

		} else {
			pivot = strs[0].charAt(0);
		}

		// check and print put the common string
		while (!hasFound) {
			for (int i = 0; i < strs.length; i++) {
				if(index>=strs[i].length()){
					System.out.println(index-1+" "+i);
					if(index-1>=0) {
                    common = strs[i].substring(0, index-1);
					}else {
						common = "";
					}
                    return common;
                }
				if (strs[i].charAt(index) == pivot) {
					// common = strs[i].substring(0, index);

				} else {
					if(index!=0) {
					common = strs[i].substring(0, index);
					hasFound = true;
					}else {
						return "";
					}
				}
				// if the loop is in the last word and the index is still in the range
				if (i == strs.length - 1 && index < strs[0].length() - 1) {
					index++;
					pivot = strs[0].charAt(index);
				}
                else if(i == strs.length - 1 && index == strs[0].length() - 1){
                    common = strs[0];
                    hasFound = true;
                }

			}
		}

		return common;

	}
}

//this is the standard soulution
class SolutionLong2 {
	public String longestCommonPrefix(String[] strs) {
		if (strs.length == 0)
			return "";
		String prefix = strs[0];
		for (int i = 1; i < strs.length; i++)
			while (strs[i].indexOf(prefix) != 0) {
				prefix = prefix.substring(0, prefix.length() - 1);
				if (prefix.isEmpty())
					return "";
			}
		return prefix;
	}
}

