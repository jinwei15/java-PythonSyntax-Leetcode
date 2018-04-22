
public class MergeTwoSortedLists {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}

class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}
}

class SolutionMergeTwoLists {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode pivot1 = l1;
		ListNode pivot2 = l2;

		if (pivot1.val == pivot2.val) {
			l1.next = pivot2;
		} else if (pivot1.val < pivot2.val) {
			pivot1 = l1.next;
		}

		return null;

	}
}

/*
 * public ListNode mergeTwoLists(ListNode l1, ListNode l2){
		if(l1 == null) return l2;
		if(l2 == null) return l1;
		if(l1.val < l2.val){
			l1.next = mergeTwoLists(l1.next, l2);
			return l1;
		} else{
			l2.next = mergeTwoLists(l1, l2.next);
			return l2;
		}
}
 * 
 * 
 * */
