import java.util.ArrayList;
import java.util.List;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class KeyboardRow {

	/**
	 * @param args
	 *            Given a List of words, return the words that can be typed using
	 *            letters of alphabet on only one row's of American keyboard like
	 *            the image below.
	 * 
	 * 
	 *            American keyboard
	 * 
	 * 
	 *            Example 1: Input: ["Hello", "Alaska", "Dad", "Peace"] Output:
	 *            ["Alaska", "Dad"]
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionKeyboardRow bb =new SolutionKeyboardRow();
		String[] myStringArray = {"Hello", "Alaska", "Dad", "Peace"};
	    bb.findWords(myStringArray);
	}

}

class SolutionKeyboardRow {
    public String[] findWords(String[] words) {
    	ArrayList<String> resultList = new ArrayList<String>();
    	String regex = "[qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*";
    //	String regex = "[asdfghjkl]*";
    	for (int i = 0; i<words.length;i++) {
    		if(words[i].toLowerCase().matches(regex)) {
    			resultList.add(words[i]);
    		}
    	}

		return resultList.toArray(new String[resultList.size()]);
        
    }
}
