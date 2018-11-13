class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        fruit_count = {}
        j = 0
        res = 0
        for i in xrange(len(tree)):
            fruit_count[tree[i]] = fruit_count.get(tree[i], 0) + 1
            while len(fruit_count) > 2:
                fruit_count[tree[j]] -= 1
                if fruit_count[tree[j]] == 0:
                    fruit_count.pop(tree[j])
                j += 1
            res = max(res, sum(fruit_count.values()))
        return res


print Solution().totalFruit([1, 2, 1])
print Solution().totalFruit([0, 1, 2, 2])
print Solution().totalFruit([1, 2, 3, 2, 2])
print Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
