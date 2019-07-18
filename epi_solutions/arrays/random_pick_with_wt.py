
import random
from bisect import bisect_left


class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.aux_w = w
        self.s = 0
        for i in w:
            self.s += i
            self.aux_w.append(self.s)

    def pickIndex(self):
        """
        :rtype: int
        """
        rand_idx = random.randint(0, self.s)
        return bisect_left(self.aux_w, rand_idx)