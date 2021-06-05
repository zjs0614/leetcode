# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    """
    Analysis:
      - fast, slow pointers
        - fast: move next 2 nodes per iter
        - slow: move next 1 node per iter
        - when fast meets slow -> there is a circle
        - otherwise no circle

      - if there is a circle, when fast slow meets at pos p-1:
        - let a = length of nodes before circle
              b = length of nodes in circle
        => p = (p * k*b) / 2 => p = k*b where k >= 1
        => a = a + b + (k-1)b - p
    """
    if not head or not head.next:
      return None
    if head.next == head:
      return head

    fast, slow = head.next, head
    while fast.next and fast.next.next and fast != slow:
      fast = fast.next.next
      slow = slow.next
    
    if not fast.next or not fast.next.next:
      return None
    else:
      slow, fast = head, fast.next
      pos = 0
      while slow != fast:
        slow, fast = slow.next, fast.next
        pos += 1
      return slow


    
        