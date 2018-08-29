# Definition for a binary tree node.
from Queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def levelorder(cls, root):
        q = Queue()
        q.put((root, 0))
        sol_dict = {}
        while q.qsize() > 0:
            node, level = q.get()
            if level not in sol_dict:
                sol_dict[level] = []
            if not node:
                sol_dict[level].append(None)
                continue
            sol_dict[level].append(node.val)
            if node.left or node.right:
                q.put((node.left, level + 1))
                q.put((node.right, level + 1))
        sol = []
        for k, v in sol_dict.iteritems():
            sol.extend(v)
        # c = 0
        # for c, i in enumerate(sol[::-1]):
        #     if i:
        #         break
        # if c > 0:
        #     return sol[:-c]
        return sol


class Solution(object):
    def generate_tree(self, start, end):
        if start > end:
            sol = [None]
        elif start == end:
            sol = [TreeNode(start)]
        else:
            sol = []
            for root in range(start, end + 1):
                left_nodes = self.generate_tree(start, root - 1)
                right_nodes = self.generate_tree(root + 1, end)

                for right_node in right_nodes:
                    for left_node in left_nodes:
                        t = TreeNode(root)
                        t.left = left_node
                        t.right = right_node
                        sol.append(t)
        if not sol:
            sol = [None]
        return sol

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        sol = self.generate_tree(1, n)
        sol_preorder = []
        for i in sol:
            sol_preorder.append(TreeNode.levelorder(i))
        return sol_preorder


# print Solution().generateTrees(3)
for i in sorted(Solution().generateTrees(4), key=lambda x: [str(j) for j in x]):
    print i
