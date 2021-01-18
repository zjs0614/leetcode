class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecursive(root, None, None)
        
    def isValidBSTRecursive(self, root: TreeNode, fromLeft: TreeNode, fromRight: TreeNode) -> bool:
        if root is None:
            return True
        
        if root.left is not None and ((root.left.val >= root.val) or \
            (fromRight is not None and fromRight.val >= root.left.val)):
            return False

        if root.right is not None and ((root.right.val <= root.val) or \
            (fromLeft is not None and fromLeft.val <= root.right.val)):
            return False
        
        return self.isValidBSTRecursive(root.left, root, fromRight) and \
                self.isValidBSTRecursive(root.right, fromLeft, root)