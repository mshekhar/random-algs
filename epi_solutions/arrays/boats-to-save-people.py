class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people or limit <= 0:
            return 0
        res = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i < j:
            if people[j] + people[i] <= limit:
                i += 1
                j -= 1
                res += 1
            else:
                res += 1
                j -= 1
        if i == j:
            res += 1
        return res


print Solution().numRescueBoats(people=[1, 2], limit=3)
print Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3)
print Solution().numRescueBoats(people=[3, 5, 3, 4], limit=5)
