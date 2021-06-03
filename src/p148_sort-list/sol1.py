# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def sortList(self, head: ListNode) -> ListNode:
    """
    Args:
      - head: listnode
    Returns:
      - ListNode: root of sorted linked list
    Constraints：
      - nums[list] -> [0, 5 * 10^4]
      - node_val: [-10^5, 10^5]
      - O(n logn) time and O(1) space

    Analysis:
      - divide and conquer, similar to merge sort for array
      - slow, fast pointers to split list
    """
    if not head or not head.next:
      return head

    slow, fast, count = self.splitNodeList(head)
    
    if count == 1:
      return self.sortTwoNodes(slow, fast)
    else:
      head1 = self.sortList(slow.next)
      slow.next = None
      head2 = self.sortList(head)

      # merge 2 sorted lists head1 and head2
      new_head, cur_node = None, None
      while head1 or head2:
        next_node, head1, head2 = \
            self.pickNextSmallestNodeFrom2SortedList(head1, head2)
        if not cur_node:
          new_head = next_node
          cur_node = new_head
        else:
          cur_node.next = next_node
          cur_node = cur_node.next
          cur_node.next = None
      return new_head

  def pickNextSmallestNodeFrom2SortedList(self, head1, head2):
    if head1 and head2:
      if head1.val < head2.val:
        return head1, head1.next, head2
      else:
        return head2, head1, head2.next
    else:
      if head1:
        return head1, head1.next, head2
      else:
        return head2, head1, head2.next
    

  def splitNodeList(self, head):
    slow, fast = head, head.next
    count = 1
    while fast and fast.next:
      count += 1
      slow = slow.next
      fast = fast.next.next
    return slow, fast, count


  def sortTwoNodes(self, node1, node2):
    if node1 and node2:
      if node1.val < node2.val:
        node1.next = node2
        node2.next = None
        return node1
      else:
        node2.next = node1
        node1.next = None
        return node2
    elif node1:
      return node1
    elif node2:
      return node2
    else:
      return None





