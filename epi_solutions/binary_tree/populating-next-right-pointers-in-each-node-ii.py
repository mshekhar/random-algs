# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def helper(self, root, parent):
        if not root:
            return
        if parent:
            next_ele = None
            if root is parent.left:
                next_ele = parent.right
            if not next_ele and parent.next:
                curr = parent.next
                next_ele = curr.left or curr.right
                while curr and not next_ele:
                    curr = curr.next
                    if curr:
                        next_ele = curr.left or curr.right
            root.next = next_ele
        self.helper(root.right, root)
        self.helper(root.left, root)
        # print root.val, root.next.val if root.next else root.next

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.helper(root, None)


def test_1():
    all_nodes = [TreeLinkNode(1)]
    root = all_nodes[-1]
    all_nodes.append(TreeLinkNode(2))
    root.left = all_nodes[-1]
    all_nodes.append(TreeLinkNode(3))
    root.right = all_nodes[-1]
    all_nodes.append(TreeLinkNode(4))
    root.left.left = all_nodes[-1]
    all_nodes.append(TreeLinkNode(5))
    root.left.right = all_nodes[-1]
    all_nodes.append(TreeLinkNode(7))
    root.right.right = all_nodes[-1]

    # print all_nodes
    Solution().connect(root)

    for i in all_nodes:
        print i.val, i.next.val if i.next else i.next


def test_2():
    all_nodes = [TreeLinkNode(1)]
    root = all_nodes[-1]

    all_nodes.append(TreeLinkNode(2))
    root.left = all_nodes[-1]
    all_nodes.append(TreeLinkNode(3))
    root.right = all_nodes[-1]

    all_nodes.append(TreeLinkNode(4))
    root.left.left = all_nodes[-1]
    all_nodes.append(TreeLinkNode(5))
    root.left.right = all_nodes[-1]
    all_nodes.append(TreeLinkNode(6))
    root.right.right = all_nodes[-1]

    all_nodes.append(TreeLinkNode(7))
    root.left.left.left = all_nodes[-1]
    all_nodes.append(TreeLinkNode(8))
    root.right.right.right = all_nodes[-1]

    # print all_nodes
    Solution().connect(root)

    for i in all_nodes:
        print i.val, i.next.val if i.next else i.next


test_1()
print '\n'
test_2()
