# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PathFound(Exception):
    def __init__(self, path):
        self.path = path


class Solution(object):
    def path_to_target(self, root, path, target):
        if not root:
            return
        path.append(root)
        if root == target:
            raise PathFound(path)
        self.path_to_target(root.left, path, target)
        self.path_to_target(root.right, path, target)
        path.pop()

    def get_distance_k_nodes(self, root, distance, res, visited):
        if not root or id(root) in visited:
            return
        if distance == 0:
            res.append(root)
            return
        if distance - 1 < 0:
            return
        visited.add(id(root))
        self.get_distance_k_nodes(root.left, distance - 1, res, visited)
        self.get_distance_k_nodes(root.right, distance - 1, res, visited)

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        path = []
        if not root:
            return []
        try:
            self.path_to_target(root, path, target)
        except PathFound:
            pass
        if not path:
            return []
        res = []
        visited = set()
        i = len(path) - 1
        available_distance = K
        while i >= 0:
            self.get_distance_k_nodes(path[i], available_distance, res, visited)
            i -= 1
            available_distance -= 1
        return map(lambda x: x.val, res)


def t1():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    target = root.left

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print Solution().distanceK(root, target, 2)


t1()
