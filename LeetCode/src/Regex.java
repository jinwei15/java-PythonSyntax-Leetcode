/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class Regex {

	/**
	 * @param args
	 *            https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String any = ".*";
		String test1 = "Hello", test2 = "29", test3 = "";

		System.out.println(test1.matches(any));
		System.out.println(test2.matches(any));
		System.out.println(test3.matches(any));
	
	}

}
