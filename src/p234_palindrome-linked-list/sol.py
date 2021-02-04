class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while True:
            if fast.next is None or fast.next.next is None:
                slow, fast = slow.next, head
                break
            else:
                fast, slow = fast.next.next, slow.next
        prev = None
        while slow is not None:
            next, slow.next, prev = slow.next, prev, slow
            slow = next
        while prev is not None and fast is not None:
            if prev.val != fast.val:
                return False
            prev, fast = prev.next, fast.next
        return True