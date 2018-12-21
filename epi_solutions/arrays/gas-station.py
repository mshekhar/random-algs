class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        start = 0
        while start < len(gas):
            tank = gas[start] - cost[start]
            if start < len(gas) - 1:
                n = start + 1
            else:
                n = 0
            # print start, n, tank
            while tank >= 0 and n != start:
                tank += gas[n] - cost[n]
                if tank < 0:
                    break
                # print start, n, tank
                if n < len(gas) - 1:
                    n += 1
                else:
                    n = 0
            # print 'ended ', start, n, tank
            if n == start:
                if tank < 0:
                    return -1
                return start
            elif n > start:
                start = n
            else:
                return -1


print Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5],
                                    cost=[3, 4, 5, 1, 2])
print Solution().canCompleteCircuit(gas=[2, 3, 4],
                                    cost=[3, 4, 3])
print Solution().canCompleteCircuit([4], [5])
