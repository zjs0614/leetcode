# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverse(self, head: ListNode, k: int, origink: int) -> ListNode:
        if k > 1 and k < origink:
            if head.next is None:
                return None, None
            else:
                next_node = head.next
                n1, n2 = self.reverse(next_node, k-1, origink)
                if n1 is not None:
                    next_node.next = head
                return n1, n2
        
        if k == origink:
            if head.next is None:
                return None, head
            else:
                next_node = head.next
                n1, n2 = self.reverse(next_node, k-1 if k > 1 else origink, origink)
                if n1 is not None:
                    next_node.next = head
                    head.next = n2
                    return None, n1
                else:
                    return None, head
        
        if k == 1:
            if head.next is None:
                return head, None
            else:
                next_node = head.next
                n1, n2 = self.reverse(next_node, origink, origink)
                return head, n2


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is not None:
            n1, n2 = self.reverse(head, k, k)
            return n2
        else:
            return head

test = Solution()

node = ListNode()
head = node
node.val = 0
for i in range(4):
    node.next = ListNode()
    node = node.next
    node.val = i + 1


result = test.reverseKGroup(head, 6)

count = 10
while result != None and count > 0:
    print(result.val)
    count = count - 1
    result = result.next