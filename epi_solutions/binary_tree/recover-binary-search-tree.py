# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def inorderTraversal(cls, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.extend(cls.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(cls.inorderTraversal(root.right))
        return res


class Solution(object):
    def __init__(self):
        self.prev_node = TreeNode(float('-inf'))
        self.node_1 = None
        self.node_2 = None

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.prev_node.val >= root.val:
            if self.node_1 is None:
                self.node_1 = self.prev_node
            self.node_2 = root
        self.prev_node = root
        self.helper(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        tmp = self.node_1.val
        self.node_1.val = self.node_2.val
        self.node_2.val = tmp


tree_1 = TreeNode(1)
tree_1.left = TreeNode(3)
tree_1.left.right = TreeNode(2)
print TreeNode.inorderTraversal(tree_1)
Solution().recoverTree(tree_1)
print TreeNode.inorderTraversal(tree_1)
print '\n\n'

tree_1 = TreeNode(3)
tree_1.left = TreeNode(1)
tree_1.right = TreeNode(4)
tree_1.right.left = TreeNode(2)
print TreeNode.inorderTraversal(tree_1)
Solution().recoverTree(tree_1)
print TreeNode.inorderTraversal(tree_1)
