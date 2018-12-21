class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        max_key = sorted_people[0][0]
        i = 0
        while i<len(sorted_people) and sorted_people[i][0] == None:
            pass


print sorted([[7, 1], [4, 4], [7, 0], [5, 0], [6, 1], [5, 2]], key=lambda x: (-x[0], x[1]))
