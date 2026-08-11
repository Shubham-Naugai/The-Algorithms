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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        int lenOfLL = 0;
        while(temp != null){
            lenOfLL++;
            temp = temp.next;
        }
        
        ListNode temp1 = head;
        int i = lenOfLL-n;
        
        while(temp1 != null){
            if (i == 0){
                head = head.next;
                return head;
            }
            if (i == 1){
                temp1.next = temp1.next.next;
                break;
            }
            i--;
            temp1 = temp1.next;
        }
        return head;
    }
}