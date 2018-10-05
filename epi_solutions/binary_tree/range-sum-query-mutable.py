class SegmentTreeNode(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.sum = 0
        self.left = None
        self.right = None

    @classmethod
    def construct_tree(cls, start, end, arr):
        if start > end:
            return None
        new_node = SegmentTreeNode()
        new_node.start = start
        new_node.end = end
        if start == end:
            new_node.sum = arr[start]
        else:
            mid = (start + end) / 2
            new_node.left = cls.construct_tree(start, mid, arr)
            new_node.right = cls.construct_tree(mid + 1, end, arr)
            if new_node.left:
                new_node.sum += new_node.left.sum
            if new_node.right.sum:
                new_node.sum += new_node.right.sum
        return new_node

    def update(self, idx, val):
        if self.start == self.end:
            # print 'update ', self.start, idx, val
            self.sum = val
            return
        mid = (self.start + self.end) / 2
        if idx <= mid:
            # print 'going left ', self.start, self.end, mid, self.left.start, self.left.end
            self.left.update(idx, val)
        else:
            self.right.update(idx, val)
        self.sum = self.left.sum + self.right.sum

    def sum_range(self, start, end):
        if self.start == start and self.end == end:
            return self.sum
        mid = (self.start + self.end) / 2
        if end <= mid:
            return self.left.sum_range(start, end)
        elif start >= mid + 1:
            return self.right.sum_range(start, end)
        else:
            return self.left.sum_range(start, mid) + self.right.sum_range(mid + 1, end)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = SegmentTreeNode.construct_tree(0, len(nums) - 1, nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.root.update(i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.root.sum_range(i, j)


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 3, 5])
print obj.sumRange(0, 2)
try:
    print obj.update(1, 2)
except:
    import time
    time.sleep(0.3)
    raise
print obj.sumRange(0, 2)
