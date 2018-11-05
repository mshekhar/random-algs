# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution(object):
    def helper(self, root, counter, most_frequent_count):
        if not root:
            return 0

        left = self.helper(root.left, counter, most_frequent_count)
        right = self.helper(root.right, counter, most_frequent_count)

        sum_subtree = left + right + root.val
        counter[sum_subtree] += 1
        most_frequent_count[0] = max(most_frequent_count[0], counter[sum_subtree])
        # print root.val, sum_subtree, most_frequent_count
        return sum_subtree

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        counter = collections.Counter()
        most_frequent_count = [float('-inf')]
        self.helper(root, counter, most_frequent_count)
        return [k for k, v in counter.items() if v == most_frequent_count[0]]


def t1():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-3)
    print Solution().findFrequentTreeSum(root)


def t2():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-5)
    print Solution().findFrequentTreeSum(root)


t1()
t2()
