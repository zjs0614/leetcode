class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        treeStr = self.traverse(root, {}, res)
        return res

    def traverse(self, root, mem, res):
        if not root:
            return '#'
        leftstr = self.traverse(root.left, mem, res)
        rightstr = self.traverse(root.right, mem, res)
        treeStr = '[' + str(root.val) + ':' + leftstr + ',' + rightstr + ']'
        found = mem[treeStr] if treeStr in mem else 0
        if found == 1:
            res.append(root)
        mem[treeStr] = found + 1
        return treeStr