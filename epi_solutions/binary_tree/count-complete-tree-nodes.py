# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_height_of_tree(self, root):
        height = 0
        curr = root
        while curr:
            height += 1
            curr = curr.left
        return height

    def helper(self, root, height, count):
        if not root:
            return count
        if not root.left and root.right:
            return count + 1
        # print 'called ', root.val, height, count
        count += 1
        path_len = 0
        curr = root.right
        while curr:
            path_len += 1
            curr = curr.left
        if path_len == height - 1:
            if root.left:
                count += (2 ** (height - 1)) - 1
            return self.helper(root.right, height - 1, count)
        else:
            if root.right:
                count += (2 ** (height - 2)) - 1
            return self.helper(root.left, height - 1, count)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = self.get_height_of_tree(root)
        return self.helper(root, height, 0)


def t1():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)

    print Solution().countNodes(root)


def t2():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(4)

    root.right = TreeNode(3)

    print Solution().countNodes(root)


t2()
t1()
