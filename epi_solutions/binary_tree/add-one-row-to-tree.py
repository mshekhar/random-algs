# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d < 1:
            return root
        if d == 1:
            tmp = TreeNode(v)
            tmp.left = root
            return tmp

        depth = 1
        level = [root]
        while level:
            # print map(lambda x: x.val, level), depth, d - 1
            if depth == d - 1:
                break
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
            depth += 1

        for node in level:
            tmp = None
            if node.left:
                tmp = node.left
            node.left = TreeNode(v)
            node.left.left = tmp
            tmp = None
            if node.right:
                tmp = node.right
            node.right = TreeNode(v)
            node.right.right = tmp

        return root

# [1,2,3,4]
# 5
# 4
