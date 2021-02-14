"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
            Loop through the whole list, and assign next pointer.
            Record each node in a map with its original node as key, new node as value -> (Node old, Node new)
            Loop through the whole list again, to assign random pointer.

            Time:  O(n)
            Space: O(n)

            Note: 
                (1) shouldn't modify original node list.
                (2) next and random node of the new nodeare all in clone list
        '''
        if head is None:
            return None
        mem, newRoot = {}, Node(head.val, None, None)
        newNode, oldNode = newRoot, head
        while oldNode is not None:
            if oldNode.next is not None:
                newNode.next = Node(oldNode.next.val)
            if oldNode.random is not None and oldNode.random in mem is not None:
                newNode.random = mem[oldNode.random]
            mem[oldNode] = newNode
            oldNode = oldNode.next
            newNode = newNode.next
        
        newNode, oldNode = newRoot, head
        while oldNode is not None:
            if oldNode.random is not None and oldNode.random in mem is not None:
                newNode.random = mem[oldNode.random]
            oldNode = oldNode.next
            newNode = newNode.next
        return newRoot





