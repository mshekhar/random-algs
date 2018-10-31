# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, root, path, res):
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append("".join(path))
        path.append("->")
        if root.left:
            self.helper(root.left, path, res)
        if root.right:
            self.helper(root.right, path, res)
        path.pop()
        path.pop()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root:
            self.helper(root, [], res)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

print Solution().binaryTreePaths(root)
