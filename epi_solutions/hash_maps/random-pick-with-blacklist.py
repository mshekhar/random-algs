import random


class Solution(object):
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist_map = {}
        for i in blacklist:
            self.blacklist_map[i] = None
        self.new_size = N - len(self.blacklist_map)
        for b in self.blacklist_map:
            if b < self.new_size:
                while N - 1 in self.blacklist_map:
                    N -= 1
                self.blacklist_map[b] = N - 1
                N -= 1

    def pick(self):
        """
        :rtype: int
        """
        r_num = random.randint(0, self.new_size - 1)
        return self.blacklist_map.get(r_num, r_num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# s = Solution(1, [])
# print s.blacklist_map, s.new_size, s.pick(), s.pick(), s.pick()
# s = Solution(2, [])
# print s.blacklist_map, s.new_size, s.pick(), s.pick(), s.pick()
# s = Solution(3, [1])
# print s.blacklist_map, s.new_size, s.pick(), s.pick(), s.pick()
# s = Solution(3, [1, 2])
# print s.blacklist_map, s.new_size, s.pick(), s.pick(), s.pick()

s = Solution(4, [0, 3])
print s.blacklist_map, s.new_size, s.pick(), s.pick(), s.pick()
