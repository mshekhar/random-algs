# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, root):
        if not root:
            return 0, 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        res_1 = max(left) + max(right)
        res_2 = root.val + left[0] + right[0]
        return res_1, res_2

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))


tree_1 = TreeNode(3)
tree_1.left = TreeNode(2)
tree_1.right = TreeNode(3)
tree_1.left.right = TreeNode(3)
tree_1.right.right = TreeNode(1)
print Solution().rob(tree_1)

tree_2 = TreeNode(3)
tree_2.left = TreeNode(4)
tree_2.right = TreeNode(5)

tree_2.left.left = TreeNode(1)
tree_2.left.right = TreeNode(3)

tree_2.right.right = TreeNode(1)
print Solution().rob(tree_2)
