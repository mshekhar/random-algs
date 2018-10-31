# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_filtered_next_level(self, level):
        first_non_null_idx = len(level) - 1
        for i in xrange(len(level)):
            if level[i] is not None:
                first_non_null_idx = i
                break

        last_non_null_idx = 0
        for i in xrange(len(level) - 1, -1, -1):
            if level[i] is not None:
                last_non_null_idx = i
                break

        return level[first_non_null_idx:last_non_null_idx + 1]

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        level = [root]
        max_width = 1
        while level:
            next_level = []
            for node in level:
                if node is None:
                    next_level.append(None)
                    next_level.append(None)
                else:
                    next_level.append(node.left)
                    next_level.append(node.right)
            # import pdb
            # pdb.set_trace()
            level = self.get_filtered_next_level(next_level)
            # print 'next level ', next_level, level
            max_width = max(max_width, len(level))
        return max_width


def t1():
    print Solution().widthOfBinaryTree(root=TreeNode(1))


def t2():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)

    root.right.right = TreeNode(9)
    print Solution().widthOfBinaryTree(root=root)


t1()
t2()
