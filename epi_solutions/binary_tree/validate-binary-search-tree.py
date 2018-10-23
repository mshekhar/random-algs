# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def is_bst_valid(self, root, min_val, max_val):
        if not root:
            return True
        elif root.val >= max_val or root.val <= min_val:
            return False
        return self.is_bst_valid(root.left, min_val, root.val) and self.is_bst_valid(root.right, root.val, max_val)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.is_bst_valid(root, float('-inf'), float('inf'))
