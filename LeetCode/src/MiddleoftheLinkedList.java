/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode[] result = new  ListNode[100];
        int index = 0;
        while(head!=null){
            result[index] = head;
            head = head.next;
            index ++;
        }
        
        return result[index/2];
    }
}
