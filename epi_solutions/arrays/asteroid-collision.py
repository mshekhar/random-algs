class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = 0
        while i < len(asteroids) and asteroids[i] < 0:
            stack.append(asteroids[i])
            i += 1
        while i < len(asteroids):
            if asteroids[i] >= 0:
                stack.append(asteroids[i])
            else:
                while stack and 0 <= stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack and stack[-1] < 0:
                    stack.append(asteroids[i])
            # print asteroids[i], stack
            i += 1
        return stack


print Solution().asteroidCollision([5, 10, -5])
print Solution().asteroidCollision([-2, -1, 1, 2])
print Solution().asteroidCollision([-2, -1, 1, -2, 3, -5, 6, -6, 7])
print Solution().asteroidCollision([8, -8])
print Solution().asteroidCollision([10, 2, -5])
