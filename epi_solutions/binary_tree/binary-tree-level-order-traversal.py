# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import Queue


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        q = Queue.Queue()
        q.put((root, 0))
        while q.qsize() > 0:
            node, level = q.get()
            while len(res) < level + 1:
                res.append([])
            res[level].append(node.val)
            if node.left:
                q.put((node.left, level + 1))
            if node.right:
                q.put((node.right, level + 1))
        return res


tree_1 = TreeNode(3)
tree_1.left = TreeNode(9)
tree_1.right = TreeNode(20)
tree_1.right.left = TreeNode(15)
tree_1.right.right = TreeNode(7)

print Solution().levelOrder(tree_1)
