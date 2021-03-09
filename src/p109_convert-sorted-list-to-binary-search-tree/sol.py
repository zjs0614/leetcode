# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        1,2,3,4,5,6
        3
       / \
       1  5
      /\  /\
       2  4 6     
        '''
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1
        return self.sortedListToBSTWithLength(head, length)
        
    def sortedListToBSTWithLength(self, head, length):
        if length < 1:
            return None
        if length == 1:
            return TreeNode(head.val)
        if length <= 3:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            root.right = TreeNode(head.next.next.val) if length == 3 else None
            return root
        
        mid = int(length / 2)
        node = head
        while mid > 1:
            node = node.next
            mid -= 1
        midNode = node.next
        node.next = None
        root = TreeNode(midNode.val)
        root.left = self.sortedListToBSTWithLength(head, int(length/2))
        root.right = self.sortedListToBSTWithLength(midNode.next, length - int(length/2) - 1)
        return root