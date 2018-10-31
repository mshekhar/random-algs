# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def helper(self, root, running_sum, res):
        running_sum = running_sum * 10 + root.val
        # print root.val, running_sum, path, running_sum == target_sum,root.left,  root.right

        if not root.left and not root.right:
            res[0] += running_sum
        if root.left:
            self.helper(root.left, running_sum, res)
        if root.right:
            self.helper(root.right, running_sum, res)
        running_sum -= root.val
        running_sum /= 10

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        if root:
            self.helper(root, 0, res)
        return res[0]
