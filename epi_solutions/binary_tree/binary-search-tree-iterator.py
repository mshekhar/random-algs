# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.path = []
        self.extract_path(self.root)

    def extract_path(self, root):
        while root:
            self.path.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.path)

    def next(self):
        """
        :rtype: int
        """
        res = self.path.pop()
        self.extract_path(res.right)
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
