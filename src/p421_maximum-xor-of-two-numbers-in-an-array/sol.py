class BitTreeNode:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # sol1 prefix_bit
        # return self.sol_prefix_bit(nums)

        # sol2 trie_Tree
        return self.sol_trie_tree(nums)

    def sol_prefix_bit(self, nums):
        max_length = len(bin(max(nums))) - 2
        res = 0
        for i in range(max_length)[::-1]:
            prefixes = {num >> i for num in nums}
            res = res << 1
            xor = res + 1
            if any(num ^ xor in prefixes for num in prefixes):
                res += 1
        return res

    def sol_trie_tree(self, nums):
        root = BitTreeNode()
        max_length = len(bin(max(nums))) - 2
        self.build_trie_tree(root, nums, max_length)
        
        left, right = root, root
        return self.find(left, right, max_length - 1)
    
    def find(self, left, right, level):
        res = 0
        if left.left is not None and right.right is not None:
            res = 1 << level
            res += self.find(left.left, right.right, level - 1)
        if left.right is not None and right.left is not None:
            res1 = 1 << level
            res1 += self.find(left.right, right.left, level - 1)
            if res1 > res:
                res = res1
        if res == 0:
            if left.left is not None and right.left is not None:
                res += self.find(left.left, right.left, level - 1)
            elif left.right is not None and right.right is not None:
                res += self.find(left.right, right.right, level - 1)
        return res

    def build_trie_tree(self, node, nums, length):
        if length <= 0:
            return
        div = 1 << (length-1)
        left = set()
        right = set()
        for num in nums:
            if num & div == div:
                left.add(num)
            else:
                right.add(num)
        if len(left) > 0:
            node.left = BitTreeNode()
            self.build_trie_tree(node.left, left, length - 1)
        if len(right) > 0:
            node.right = BitTreeNode()
            self.build_trie_tree(node.right, right, length - 1)
