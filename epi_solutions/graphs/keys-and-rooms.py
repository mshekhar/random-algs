class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        stack = []
        visited = set()
        visited.add(0)
        stack.append(0)
        while stack:
            i = stack.pop()
            for j in rooms[i]:
                if j not in visited:
                    stack.append(j)
                    visited.add(j)
                    if len(visited) == len(rooms):
                        return True
        return len(visited) == len(rooms)


print Solution().canVisitAllRooms([[1], [2], [3], []])
print Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
