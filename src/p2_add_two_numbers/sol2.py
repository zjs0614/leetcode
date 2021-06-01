# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    """
    Args:
      - l1, l2: reversed ordered non-negative integers
    Returns:
      - ListNode: reversed order of sum integer (l1 + l2)
    Analysis:
      - linked node list traverse problem
      - combine two linked list to one with plus rule
    Special Cases:
      - if l1[i] + l2[i] >= 10 carry 1 addition to next node at i+1,
        and if no i+1 th node in l1 and l2, create a new node
      - either l1 or l2 reached to the end, append rest to the current tail
    """
    if not l1 and not l2:
      return None
    elif not l1:
      return l2
    elif not l2:
      return l1

    res = ListNode()
    cur, carry = None, 0
    while l1 or l2 or carry == 1:
      if not cur:
        cur = res
      else:
        cur.next = ListNode()
        cur = cur.next

      if l1 and l2:
        cur.val, carry = (l1.val + l2.val + carry) % 10, int((l1.val + l2.val + carry) / 10)

      elif l1 or l2:
        remain = l1 if l1 else l2

        if carry == 0:
          cur.val = remain.val
          cur.next = remain.next
          break
        else:
          cur.val, carry = (remain.val + carry) % 10, int((remain.val + carry) / 10)

      else:
        cur.val = 1
        carry = 0

      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
  
    return res