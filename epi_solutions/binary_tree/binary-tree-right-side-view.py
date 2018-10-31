# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        level = [root]
        while level:
            res.append(level[-1].val)
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return res


def test_1():
    all_nodes = [TreeNode(1)]
    root = all_nodes[-1]
    all_nodes.append(TreeNode(2))
    root.left = all_nodes[-1]
    all_nodes.append(TreeNode(3))
    root.right = all_nodes[-1]
    all_nodes.append(TreeNode(4))
    root.left.left = all_nodes[-1]
    all_nodes.append(TreeNode(5))
    root.left.right = all_nodes[-1]
    all_nodes.append(TreeNode(7))
    root.right.right = all_nodes[-1]

    # print all_nodes
    print Solution().rightSideView(root)


def test_2():
    all_nodes = [TreeNode(1)]
    root = all_nodes[-1]

    all_nodes.append(TreeNode(2))
    root.left = all_nodes[-1]
    all_nodes.append(TreeNode(3))
    root.right = all_nodes[-1]

    all_nodes.append(TreeNode(4))
    root.left.left = all_nodes[-1]
    all_nodes.append(TreeNode(5))
    root.left.right = all_nodes[-1]
    all_nodes.append(TreeNode(6))
    root.right.right = all_nodes[-1]

    all_nodes.append(TreeNode(7))
    root.left.left.left = all_nodes[-1]
    all_nodes.append(TreeNode(8))
    root.right.right.right = all_nodes[-1]

    # print all_nodes
    print Solution().rightSideView(root)


test_1()
test_2()
