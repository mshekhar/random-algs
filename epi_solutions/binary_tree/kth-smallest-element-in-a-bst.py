# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class ElementFoundException(Exception):
    def __init__(self, val, *args):
        self.val = val
        super(ElementFoundException, self).__init__(*args)


class Solution(object):
    def helper(self, root, k):
        if not root:
            return 0
        ele_count_left = self.helper(root.left, k)
        if k - ele_count_left == 1:
            raise ElementFoundException(root.val)
        ele_count_right = self.helper(root.right, k - ele_count_left - 1)
        return ele_count_left + ele_count_right + 1

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        try:
            self.helper(root, k)
        except ElementFoundException, e:
            return e.val
