class Solution(object):
    @classmethod
    def people_comparator(cls):
        def compare(person_1, person_2):
            if person_1[0] == person_2[0]:
                return cmp(person_1[1], person_2[1])
            return cmp(-person_1[0], -person_2[0])

        return compare

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(people, cmp=self.people_comparator())
        res = []
        for p in sorted_people:
            res.insert(p[1], p)
        return res


print Solution().reconstructQueue([[7, 1], [4, 4], [7, 0], [5, 0], [6, 1], [5, 2]])
