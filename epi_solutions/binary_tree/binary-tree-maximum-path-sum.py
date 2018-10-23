# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, max_sum):
        if not root:
            return 0
        left_sum = self.helper(root.left, max_sum)
        right_sum = self.helper(root.right, max_sum)
        if left_sum < 0:
            left_sum = 0
        if right_sum < 0:
            right_sum = 0
        path_sum = left_sum + right_sum + root.val
        max_sum[0] = path_sum if path_sum > max_sum[0] else max_sum[0]
        return root.val + max(left_sum, right_sum)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('-inf')]
        self.helper(root, res)
        return res[0]
