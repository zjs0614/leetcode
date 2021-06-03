# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      - fast slow pointers
      - special cases:
        - [1], 1
        - [1,2], 2
    """

    fast, size = head, n
    while size > 1 and fast:
      fast = fast.next
      size -= 1

    if not fast.next: # when fast reach end, len(nodelist) == n
      return head.next
    else:
      fast = fast.next
    
    slow = head
    while fast.next:
      slow = slow.next
      fast = fast.next
    
    slow.next = slow.next.next
    return head
    