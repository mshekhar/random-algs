# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def pre_order_with_null(self, root, counter, res):
        if not root:
            return str(None)
        hash_key = "_".join([self.pre_order_with_null(root.left, counter, res),
                             self.pre_order_with_null(root.right, counter, res),
                             str(root.val)])
        if counter[hash_key] == 1:
            res.append(root)
        counter[hash_key] += 1
        return hash_key

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        counter = collections.Counter()
        res = []
        self.pre_order_with_null(root, counter, res)
        return res
