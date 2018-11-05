# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        q = Queue.Queue()
        q.put(root)
        last_node = None
        while q.qsize() > 0:
            node = q.get()
            if node.right:
                q.put(node.right)
            if node.left:
                q.put(node.left)
            last_node = node
        return last_node.val
