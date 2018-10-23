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
    def postorderTraversal(cls, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if not root:
            return res
        res.extend(cls.postorderTraversal(root.left))
        res.extend(cls.postorderTraversal(root.right))
        res.append(root.val)
        return res


class Solution(object):
    def construct(self, inorder_map, postorder, inorder_start, inorder_end):
        if not postorder:
            return None
        root = TreeNode(postorder.pop())
        root_idx = inorder_map[root.val]
        # right node
        if not postorder:
            return root
        potential_right = postorder[-1]
        potential_right_idx = inorder_map[potential_right]
        if root_idx < potential_right_idx < inorder_end:
            root.right = self.construct(inorder_map, postorder, root_idx, inorder_end)

        # left node
        if not postorder:
            return root
        potential_left = postorder[-1]
        potential_left_idx = inorder_map[potential_left]
        if inorder_start < potential_left_idx < root_idx:
            root.left = self.construct(inorder_map, postorder, inorder_start, root_idx)

        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.construct({k: c for c, k in enumerate(inorder)}, postorder, -1, len(inorder))


res = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print TreeNode.inorderTraversal(res), [9, 3, 15, 20, 7]
print TreeNode.postorderTraversal(res), [9, 15, 7, 20, 3]

res = Solution().buildTree([9, 8], [9, 8])
print TreeNode.inorderTraversal(res), [9, 8]
print TreeNode.postorderTraversal(res), [9, 8]
