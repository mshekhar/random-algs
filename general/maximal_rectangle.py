class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[self.size() - 1]
        else:
            return None

    def size(self):
        return len(self.items)


class Solution(object):
    def __init__(self):
        self.pos_stack = Stack()
        self.height_stack = Stack()

    def getMaxAreaFromStack(self, h, c, max_area=0):
        head_pos = head_height = -1
        # print h, c, max_area, self.pos_stack.items, self.height_stack.items
        while h < self.height_stack.peek():
            head_height = self.height_stack.pop()
            head_pos = self.pos_stack.pop()
            area = head_height * (c - head_pos)
            if area > max_area:
                max_area = area
        return max_area, head_pos, head_height

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        c = 0
        h = -1
        for c, h in enumerate(heights, start=1):
            if self.height_stack.peek() is None or h > self.height_stack.peek():
                self.height_stack.push(h)
                self.pos_stack.push(c)
            elif h < self.height_stack.peek():
                max_area, head_pos, head_height = self.getMaxAreaFromStack(h, c, max_area=max_area)
                self.height_stack.push(h)
                self.pos_stack.push(head_pos)
        if self.height_stack.size() > 0:
            max_area, head_pos, head_height = self.getMaxAreaFromStack(-1, c + 1, max_area=max_area)
        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        if matrix:
            running_mtx = map(lambda x: int(x), matrix[0])
            for i in range(len(matrix)):
                row_i = matrix[i]
                if i > 0:
                    for j in range(len(row_i)):
                        running_mtx[j] = 0 if not int(row_i[j]) else running_mtx[j] + 1
                area = self.largestRectangleArea(running_mtx)
                if area > max_area:
                    max_area = area
        return max_area


print Solution().maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
])
# print Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
# print Solution().largestRectangleArea([2])
# print Solution().largestRectangleArea([2, 1, 2])
