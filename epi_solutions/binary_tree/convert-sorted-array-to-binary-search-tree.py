# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def inorderTraversal(cls, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.extend(cls.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(cls.inorderTraversal(root.right))
        return res


class Solution(object):
    def helper(self, nums, start_idx, end_idx):
        if end_idx < start_idx:
            return
        mid_val = (end_idx + start_idx) / 2
        root = TreeNode(nums[mid_val])
        root.left = self.helper(nums, start_idx, mid_val - 1)
        root.right = self.helper(nums, mid_val + 1, end_idx)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)


res = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print TreeNode.inorderTraversal(res), [-10, -3, 0, 5, 9]
