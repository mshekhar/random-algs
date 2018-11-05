# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        stack = []
        max_node = None
        for n in nums:
            curr = TreeNode(n)
            if not max_node or n > max_node.val:
                max_node = curr
            while stack and stack[-1].val < n:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)

        return max_node
