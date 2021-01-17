package src.p2_add_two_numbers;

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
      ListNode root = new ListNode(0);
      ListNode currentNode = root;
      int carry = 0;

      while (l1 != null || l2 != null || carry > 0) {
          int value = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
          carry = value >= 10 ? 1 : 0;
          currentNode.next = new ListNode(value % 10);
          currentNode = currentNode.next;
          l1 = l1 != null ? l1.next : null;
          l2 = l2 != null ? l2.next : null;
      }
      return root.next;
  }
}