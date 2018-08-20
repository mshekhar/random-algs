import hashlib
import marshal


class Solution(object):
    def val_hash_func(self, x):
        return x
        return hashlib.md5(marshal.dumps(x)).hexdigest()

    def is_idx_valid(self, k1, k2, mtx):
        if k1 < 0 or k2 < 0:
            return False
        try:
            _ = mtx[k1][k2]
        except IndexError:
            return False
        return True

    def get_valid_neighbors(self, i, j, mtx):
        for k1, k2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if self.is_idx_valid(k1, k2, mtx):
                yield k1, k2

    def init_out_of_boundary_ways(self, m, n):
        mtx = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                c = 0
                for k1, k2 in self.get_valid_neighbors(i, j, mtx):
                    c += 1
                mtx[i][j] = 4 - c
        return mtx

    def helper(self, c1, c2, n, N, mtx, dp):
        hash_key = self.val_hash_func((c1, c2, n))
        if hash_key not in dp:
            paths = 0
            if n <= N:
                paths += mtx[c1][c2]
                for k1, k2 in self.get_valid_neighbors(c1, c2, mtx):
                    paths += self.helper(k1, k2, n + 1, N, mtx, dp)
            dp[hash_key] = paths
        return dp[hash_key]

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        # if m == 8 and n == 50 and N == 23 and i == 5 and j == 26:
        #     return 914783380
        mtx = self.init_out_of_boundary_ways(m, n)
        dp = {}
        paths = self.helper(i, j, 1, N, mtx, dp)
        mod_den = (10 ** 9) + 7
        # q = Queue()
        #
        # q.put((i, j))
        # paths = 0
        # for n in range(1, N + 1):
        #     q2 = Queue()
        #     while q.qsize() > 0:
        #         c1, c2 = q.get()
        #         paths += mtx[c1][c2]
        #         # print n, c1, c2, mtx[c1][c2], paths
        #         for k1, k2 in self.get_valid_neighbors(c1, c2, mtx):
        #             q2.put((k1, k2))
        #     q = q2
        return paths % mod_den


print Solution().findPaths(2, 2, 2, 0, 0)
print Solution().findPaths(1, 3, 3, 0, 1)
print Solution().findPaths(8, 50, 23, 5, 26)
