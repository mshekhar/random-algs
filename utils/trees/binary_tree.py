from utils.trees.base import NodeBase


class BinaryTreeNode(NodeBase):
    def __init__(self, **kwargs):
        self._left = kwargs.pop('left', None)
        self._right = kwargs.pop('right', None)
        super(BinaryTreeNode, self).__init__(**kwargs)
        self.add_child(self.left)
        self.add_child(self.right)

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left
        self.modify_child(0, left)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right
        self.modify_child(1, right)

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            yield node
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node):
        if node is not None:
            yield node
            self.traverse_inorder(node.left)
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            self.traverse_inorder(node.right)
            yield node

    def add_child(self, child, left_child=True, raise_if_not_empty=False):
        index = 0
        if left_child:
            if self.left is not None and raise_if_not_empty:
                raise ValueError('node left not empty')
            self.left = child
        else:
            if self.right is not None and raise_if_not_empty:
                raise ValueError('node right not empty')
            index = 1
            self.right = child
        self.modify_child(index=index, new_child=child)
