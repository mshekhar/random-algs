# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, root, new_node):
        if not root:
            return new_node
        if new_node.val > root.val:
            root.right = self.helper(root.right, new_node)
        else:
            root.left = self.helper(root.left, new_node)
        return root

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        return self.helper(root, new_node)
