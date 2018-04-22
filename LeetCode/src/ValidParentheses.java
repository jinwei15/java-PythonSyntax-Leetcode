import java.util.Stack;

/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class ValidParentheses {

	/**
	 * @param args
	 * 
	 *            Given a string containing just the characters '(', ')', '{', '}',
	 *            '[' and ']', determine if the input string is valid.
	 * 
	 *            An input string is valid if:
	 * 
	 *            Open brackets must be closed by the same type of brackets. Open
	 *            brackets must be closed in the correct order. Note that an empty
	 *            string is also considered valid.
	 * 
	 *            Example 1:
	 * 
	 *            Input: "()" Output: true
	 * 
	 *            Example 2:
	 * 
	 *            Input: "()[]{}" Output: true
	 * 
	 *            Example 3:
	 * 
	 *            Input: "(]" Output: false
	 * 
	 *            Example 4:
	 * 
	 *            Input: "([)]" Output: false
	 * 
	 *            Example 5:
	 * 
	 *            Input: "{[]}" Output: true
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionVaild fuck = new SolutionVaild();
		boolean flag = fuck.isValid("()");
		System.out.println(flag);
	}

}
// loop through the string and find the matched characters

class SolutionVaild {
	public boolean isValid(String s) {
		if(s.length()%2 != 0) return false;
		Stack<Character> numberSt = new Stack<Character>();
		// numberSt.push(s.charAt(0));

		for (int i = 0; i < s.length(); i++) {
			// Character c = new Character(s.charAt(i));
			switch (s.charAt(i)) {
			case '(':
				numberSt.push('(');
				break;

			case '{':
				numberSt.push('{');
				break;

			case '[':
				numberSt.push('[');
				break;
			case ')':
				if (numberSt.size() == 0||!numberSt.pop().equals('(')) {
                      return false;
				}
				break;
			case '}':
				if (numberSt.size() == 0||!numberSt.pop().equals('{')) {
					 return false;
				}
				break;
			case ']':
				if (numberSt.size() == 0||!numberSt.pop().equals('[')) {
					 return false;
				}
				break;
			default:
				break;
			}
		}

		return true;

	}
}
