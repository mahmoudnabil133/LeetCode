/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur1 = l1, cur2 = l2, prev = null;

        int sum = 0, dig = 0, carry = 0;
        while(cur1 != null && cur2 !=null){
            sum = (cur1.val + cur2.val + carry);
            dig = sum % 10;
            carry = sum / 10;
            cur1.val = dig;
            prev = cur1;
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
        if(cur1 != null){
            LoopList(cur1, prev, carry);

        } else if(cur2 != null){
            prev.next = cur2;
            LoopList(cur2, prev, carry);

        } else if(carry > 0){
            prev.next = new ListNode(1);
        }

        return l1;
    }
    
    public void LoopList(ListNode cur, ListNode prev, int carry){
        int sum = 0, dig = 0;
        while(cur != null && carry > 0){
            sum = cur.val + carry;
            dig = sum % 10;
            cur.val = dig;
            carry = sum / 10;
            prev = cur;
            cur = cur.next;
        }
        if (carry > 0){
            prev.next = new ListNode(1);
        }
    }
}