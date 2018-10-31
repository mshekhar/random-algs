# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if not root:
            return []
        level = [root]
        max_val = root.val
        while level:
            res.append(max_val)
            max_val = float('-inf')
            next_level = []
            for node in level:
                if node.left:
                    max_val = max(max_val, node.left.val)
                    next_level.append(node.left)
                if node.right:
                    max_val = max(max_val, node.right.val)
                    next_level.append(node.right)
            level = next_level
        return res
