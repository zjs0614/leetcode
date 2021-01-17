class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        root = ListNode()
        currentNode = root

        while l1 or l2 or carry:
            carry, value = divmod((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry, 10)
          
            currentNode.next = ListNode(value)
            currentNode = currentNode.next

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        return root.next