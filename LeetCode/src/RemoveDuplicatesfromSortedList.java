/**
 * 
 */

/**
 * @author sgjzha34
 *
 */
public class RemoveDuplicatesfromSortedList {

	/**
	 * @param args
	 *            Given a sorted linked list, delete all duplicates such that each
	 *            element appear only once.
	 * 
	 *            Example 1:
	 * 
	 *            Input: 1->1->2 
	 *            Output: 1->2 Example 2:
	 * 
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
	}

}


//  Definition for singly-linked list.
  class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
 
  }
  
  //I will start this in the simplest way
class SolutionRemoveDuplicatesfromSortedList {
    public ListNode deleteDuplicates(ListNode head) {

    	ListNode current =  head;
    	
    	while (current != null && current.next!=null) {
    		if(current.next.val == current.val ) {
    			//next next could be null
        		current.next = current.next.next;
        	}else {
        		current = current.next;
        	}
    	}
    	
    	
		return head;
        
    }
}
