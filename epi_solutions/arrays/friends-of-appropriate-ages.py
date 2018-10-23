class Solution(object):
    def can_request(self, a, b):
        return not (b <= (0.5 * a) + 7 or b > a or b > 100 > a)

    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        uniq_age_counters = {}
        for i in ages:
            if i not in uniq_age_counters:
                uniq_age_counters[i] = 0
            uniq_age_counters[i] += 1

        res = 0
        for a in uniq_age_counters:
            for b in uniq_age_counters:
                if self.can_request(a, b):
                    res += uniq_age_counters[a] * uniq_age_counters[b]
                    if a == b:
                        res -= uniq_age_counters[a]
        return res


print Solution().numFriendRequests([16])
print Solution().numFriendRequests([])
print Solution().numFriendRequests([16, 16])
print Solution().numFriendRequests([16, 17, 18])
print Solution().numFriendRequests([20, 30, 100, 110, 120])
