class Solution(object):
    def jump(self, arr):
        # The number of jumps needed to reach the starting index is 0
        n = len(arr)
        if n <= 1:
            return 0

        # Return -1 if not possible to jump
        if arr[0] == 0:
            return -1

        # initialization
        # stores all time the maximal reachable index in the array
        maxReach = arr[0]
        # stores the number of steps we can still take
        step = arr[0]
        # stores the number of jumps necessary to reach that maximal reachable position
        jump = 1

        # Start traversing the array

        for i in range(1, n):
            # Check if we have reached the end of the array
            if i == n - 1:
                return jump

            # updating maxReach
            maxReach = max(maxReach, i + arr[i])

            # we use a step to get to the current index
            step -= 1

            # If no further steps left
            if step == 0:
                # we must have used a jump
                jump += 1

                # Check if the current index/position or lesser index
                # is the maximum reach point from the previous indexes
                if i >= maxReach:
                    return -1

                # re-initialize the steps to the amount
                # of steps to reach maxReach from position i.
                step = maxReach - i
        return -1

    def jump_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = [0]
        for i in range(1, len(nums)):
            min_jumps = float('inf')
            for j in range(i):
                # print i, j, nums[j - 1], bool(j + nums[j] >= i), min_jumps, min(min_jumps, jumps[j] + 1)
                if j + nums[j] >= i:
                    min_jumps = min(min_jumps, jumps[j] + 1)
            jumps.append(min_jumps)
            # print jumps
        return jumps[-1]


# TODO O(n) sol
print Solution().jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]), 3
print Solution().jump([2, 3, 1, 1, 4]), 2
print Solution().jump([1, 2]), 1
