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
        left_depth, left_deepeset_node = self.helper(root.left)
        right_depth, right_deepeset_node = self.helper(root.right)
        if left_depth == right_depth:
            return left_depth + 1, root
        elif left_depth > right_depth:
            return left_depth + 1, left_deepeset_node
        else:
            return right_depth + 1, right_deepeset_node

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)
