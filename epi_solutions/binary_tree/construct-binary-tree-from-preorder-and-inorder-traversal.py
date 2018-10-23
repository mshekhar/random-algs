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

    @classmethod
    def preOrderTraversal(cls, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if not root:
            return res
        res.append(root.val)
        res.extend(cls.preOrderTraversal(root.left))
        res.extend(cls.preOrderTraversal(root.right))
        return res


class Solution(object):
    def construct(self, inorder_map, preorder, inorder_start, inorder_end, preorder_idx):
        if preorder_idx[0] >= len(preorder):
            return None
        root = TreeNode(preorder[preorder_idx[0]])
        root_idx = inorder_map[root.val]
        preorder_idx[0] += 1

        # left node
        if preorder_idx[0] >= len(preorder):
            return root
        potential_left = preorder[preorder_idx[0]]
        potential_left_idx = inorder_map[potential_left]
        if inorder_start < potential_left_idx < root_idx:
            root.left = self.construct(inorder_map, preorder, inorder_start, root_idx, preorder_idx)

        # right node
        if preorder_idx[0] >= len(preorder):
            return root
        potential_right = preorder[preorder_idx[0]]
        potential_right_idx = inorder_map[potential_right]
        if root_idx < potential_right_idx < inorder_end:
            root.right = self.construct(inorder_map, preorder, root_idx, inorder_end, preorder_idx)

        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_idx = [0]
        return self.construct({k: c for c, k in enumerate(inorder)}, preorder, -1, len(inorder), preorder_idx)


res = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print TreeNode.inorderTraversal(res), [9, 3, 15, 20, 7]
print TreeNode.preOrderTraversal(res), [3, 9, 20, 15, 7]

res = Solution().buildTree([9, 8], [9, 8])
print TreeNode.inorderTraversal(res), [9, 8]
print TreeNode.preOrderTraversal(res), [9, 8]
