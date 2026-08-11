/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null){
            return head;
        }
        ListNode evenLL = null;
        ListNode headOfEvenLL = null;

        ListNode temp = head;
        while(temp != null && temp.next != null){
            ListNode curr = temp.next.next;
            if (evenLL == null){
                evenLL = new ListNode(temp.next.val);
                headOfEvenLL = evenLL;
            }
            else{
                evenLL.next = new ListNode(temp.next.val);
                evenLL = evenLL.next;
            }
            temp.next = curr;
            if (temp.next != null){
                temp = temp.next;
            }
        }
        temp.next = headOfEvenLL;
        return head;
    }
}