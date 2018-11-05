# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def helper(self, root):
        if not root:
            return 0, None
        left_sum, root.left = self.helper(root.left)
        right_sum, root.right = self.helper(root.right)
        if left_sum + right_sum + root.val == 0:
            return 0, None
        return left_sum + right_sum + root.val, root

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[1]
