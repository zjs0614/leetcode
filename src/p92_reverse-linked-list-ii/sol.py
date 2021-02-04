class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count, prev_tail, cur, prev, tail = 0, None, head, None, None
        while count < n and cur is not None:
            next = cur.next
            if count >= m-1:
                if count == m-1:
                    tail = cur
                cur.next, prev = prev, cur
            else:
                prev_tail = cur
            cur, count = next, count + 1

        if prev_tail is not None:
            prev_tail.next = prev
        if tail is not None:
            tail.next = cur
        return head if m > 1 else prev