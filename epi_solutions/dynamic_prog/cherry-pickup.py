class GridNode(object):
    def __init__(self):
        self.starting_val = None
        self.updated_val = None
        self.right_visited = False
        self.left_visited = False
        self.top_visited = False
        self.bottom_visited = False


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
