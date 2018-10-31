# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lca_helper(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lca_helper(root.left, p, q)
        right = self.lca_helper(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        return right

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lca_helper(root, p, q)
