# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def helper(self, root, running_sum, path, res, target_sum):
        path.append(root.val)
        running_sum += root.val
        # print root.val, running_sum, path, running_sum == target_sum,root.left,  root.right

        if not root.left and not root.right and running_sum == target_sum:
            res.append(path[:])
        if root.left:
            self.helper(root.left, running_sum, path, res, target_sum)
        if root.right:
            self.helper(root.right, running_sum, path, res, target_sum)
        running_sum -= root.val
        path.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root:
            self.helper(root, 0, [], res, sum)
        return res
