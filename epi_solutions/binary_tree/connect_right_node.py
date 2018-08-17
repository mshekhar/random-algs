from utils.trees.binary_tree import BinaryTreeNode


# http://www.geeksforgeeks.org/connect-nodes-at-same-level-with-o1-extra-space/

class NextRightNode(BinaryTreeNode):
    def __init__(self, **kwargs):
        self.next_right = kwargs.get('next_right')
        super(NextRightNode, self).__init__(**kwargs)

    def get_next_right(self, node):
        if node is None:
            return node
        tmp = node.next_right
        while tmp is not None:
            if tmp.left is not None:
                return tmp.left
            elif tmp.right is not None:
                return tmp.right
            return self.get_next_right(tmp.next_right)

    def connect_next_right_recursive(self, node):
        if node is None:
            return node
        if node.next_right is not None:
            self.connect_next_right_recursive(node.next_right)
        if node.left is not None:
            if node.right is not None:
                node.left.next_right = node.right
                node.right.next_right = self.get_next_right(node)
            else:
                node.left.next_right = self.get_next_right(node)
            self.connect_next_right_recursive(node.left)
        elif node.right is not None:
            if node.right is not None:
                node.right.next_right = self.get_next_right(node)
                self.connect_next_right_recursive(node.right)
        else:
            self.connect_next_right_recursive(self.get_next_right(node))


if __name__ == "__main__":
    nxt_tree = NextRightTree()
    nxt_tree.insert(None, 10)
    nxt_tree.insert(nxt_tree.root, 8, left_child=True)
    nxt_tree.insert(nxt_tree.root, 2, left_child=False)
    nxt_tree.insert(nxt_tree.root.left, 3, left_child=True)
    nxt_tree.insert(nxt_tree.root.right, 90, left_child=False)
    nxt_tree.connect_next_right_recursive(nxt_tree.root)
    print 'next right ', nxt_tree.root.data, nxt_tree.root.next_right.data
    print 'next right ', nxt_tree.root.left.data, nxt_tree.root.left.next_right.data
    print 'next right ', nxt_tree.root.right.data, nxt_tree.root.right.next_right.data
    print 'next right ', nxt_tree.root.left.left.data, nxt_tree.root.left.left.next_right.data
    print 'next right ', nxt_tree.root.right.right.data, nxt_tree.root.right.right.next_right.data

    n0 = NextRightNode(data=10)
    n0_l = NextRightNode(data=8)
    n0_r = NextRightNode(data=2)
    n0_l_l = NextRightNode(data=3)
    n0_r_r = NextRightNode(data=90)

    n0.add_child(n0_l, left_child=True)
    n0.add_child(n0_r, left_child=False)
    n0_l.add_child(n0_l_l, left_child=True)
    n0_r.add_child(n0_r_r, left_child=False)
    n0.pretty_print()
