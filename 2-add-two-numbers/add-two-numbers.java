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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode res = null;
        ListNode resHead = null;
        while (l1 != null && l2 != null) {
            int val = l1.val + l2.val + carry;
            carry = val/10;
            val = val%10;
            if (res == null){
                res = new ListNode(val);
                resHead = res;
            }
            else{
                res.next = new ListNode(val);
                res = res.next;
            }
            l1 = l1.next;
            l2 = l2.next;
        }

        if (l1 != null) {
            while (l1 != null) {
                int val = l1.val + carry;
                carry = val/10;
                val = val%10;
                res.next = new ListNode(val);
                res = res.next;
                l1 = l1.next;
            }
        }

        if (l2 != null) {
            while (l2 != null) {
                int val = l2.val + carry;
                carry = val/10;
                val = val%10;
                res.next = new ListNode(val);
                res = res.next;
                l2 = l2.next;
            }
        }
        if (carry > 0){
            res.next = new ListNode(carry);
        }
        return resHead;
    }
}