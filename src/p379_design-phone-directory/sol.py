class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.avail_nums = ListNode(-1)
        self.unavail_nums = ListNode(-1)
        self.numbers = [[None, True] for _ in range(maxNumbers)]
        node = self.avail_nums
        for i in range(maxNumbers):
            self.numbers[i][0] = node
            node.next = ListNode(i)
            node = node.next


    '''
    1,2,3,4
    [Node(-1), Node(1), Node(2), Node(3), Node(4)]
    [Node(-1)]
    [Node(-1), Node(1), Node(2), Node(3)]
    '''
    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.avail_nums.next is not None:
            node = self.avail_nums.next
            self.avail_nums.next = node.next
            node.next = self.unavail_nums.next
            self.unavail_nums.next = node

            self.numbers[node.val][1] = False
            self.resetPrev(self.avail_nums)
            self.resetPrev(self.unavail_nums)
            self.resetPrev(node)
            return node.val

        else:
            return -1


    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return (number < len(self.numbers)) and self.numbers[number][1]


    '''
    1,2,3,4
    [Node(-1), Node(1), Node(2), Node(3), Node(4)]
    [Node(-1)]
    [Node(-1), Node(1), Node(2), Node(3)]
    '''
    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number < len(self.numbers) and not self.numbers[number][1]:
            prev = self.numbers[number][0]
            node = prev.next
            prev.next = node.next
            node.next = self.avail_nums.next
            self.avail_nums.next = node

            self.numbers[node.val][1] = True

            self.resetPrev(prev)
            self.resetPrev(self.avail_nums)
            self.resetPrev(node)

    def resetPrev(self, node):
        if node is not None and node.next is not None:
            self.numbers[node.next.val][0] = node

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)