import collections
import math


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """

        counter = collections.Counter(answers)
        min_rabbits = 0
        for ans, count in counter.iteritems():
            # print count, ans, (ans + 1) * math.ceil(count * 1.0 / (ans + 1))
            min_rabbits += int((ans + 1) * math.ceil(count * 1.0 / (ans + 1)))
        return min_rabbits


print Solution().numRabbits([1, 1, 2])
print Solution().numRabbits([10, 10, 10])
