class TreeNode(object):
    def __init__(self, x):
        self.key = x
        self.freq = 1
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
        res.append((root.key, root.freq))
        res.extend(cls.inorderTraversal(root.right))
        return res


class BST(object):
    def __init__(self):
        self.root = None

    def find_maximum(self, root):
        while root and root.right:
            root = root.right
        return root

    def find_minimum(self, root):
        while root and root.left:
            root = root.left
        return root

    def bst_insert_helper(self, root, new_node):
        if not root:
            return new_node
        if new_node.key > root.key:
            root.right = self.bst_insert_helper(root.right, new_node)
        else:
            root.left = self.bst_insert_helper(root.left, new_node)
        return root

    def bst_search_helper(self, root, val):
        curr = root
        while curr:
            if val == curr.key:
                return curr
            elif val < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def get_successor(self, root, key, successor):
        if not root:
            return
        if root.key == key and root.right:
            successor[0] = self.find_minimum(root.left)
        elif key < root.key:
            successor[0] = root
            self.get_successor(root.left, key, successor)
        else:
            self.get_successor(root.right, key, successor)

    def get_predecessor(self, root, key, predecessor):
        if not root:
            return
        if root.key == key and root.left:
            predecessor[0] = self.find_maximum(root.left)
        elif key > root.key:
            predecessor[0] = root
            self.get_predecessor(root.right, key, predecessor)
        else:
            self.get_predecessor(root.left, key, predecessor)
