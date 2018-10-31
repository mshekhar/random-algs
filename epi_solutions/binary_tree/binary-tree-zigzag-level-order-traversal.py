import Queue


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
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

        i = 0
        while i < len(res):
            if i % 2:
                res[i] = res[i][::-1]
            i += 1
        return res
