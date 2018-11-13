class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        stack = []
        i = 0
        sorted_list = sorted(zip(position, speed), key=lambda x: x[0])
        while i < len(sorted_list):
            time_to_reach = (target - sorted_list[i][0]) * 1.0 / sorted_list[i][1]
            while stack and time_to_reach >= stack[-1]:
                stack.pop()
            stack.append(time_to_reach)
            i += 1

        return len(stack)


print Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
print Solution().carFleet(target=12, position=[10, 8, 0, 5, 3, 11], speed=[2, 4, 1, 1, 3, 0.05])
print Solution().carFleet(10, [6, 8], [3, 2])
print Solution().carFleet(10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4])
