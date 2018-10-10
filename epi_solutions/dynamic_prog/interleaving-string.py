class Solution(object):
    def get_str(self, s, idx):
        if 0 <= idx < len(s):
            return s[idx]
        return None

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        m = len(s1)
        n = len(s2)
        mtx = [[False for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(m + 1):
            for j in xrange(n + 1):
                if not i and not j:
                    mtx[i][j] = True
                elif not i and self.get_str(s2, j - 1) == self.get_str(s3, j - 1):
                    mtx[i][j] = mtx[i][j - 1]
                elif not j and self.get_str(s1, i - 1) == self.get_str(s3, i - 1):
                    mtx[i][j] = mtx[i - 1][j]
                elif self.get_str(s1, i - 1) == self.get_str(s3, i + j - 1) and \
                        self.get_str(s2, j - 1) != self.get_str(s3, i + j - 1):
                    mtx[i][j] = mtx[i - 1][j]
                elif self.get_str(s1, i - 1) != self.get_str(s3, i + j - 1) and \
                        self.get_str(s2, j - 1) == self.get_str(s3, i + j - 1):
                    mtx[i][j] = mtx[i][j - 1]
                elif self.get_str(s1, i - 1) == self.get_str(s3, i + j - 1) and \
                        self.get_str(s2, j - 1) == self.get_str(s3, i + j - 1):
                    mtx[i][j] = mtx[i][j - 1] or mtx[i - 1][j]
                print mtx[i][j], i, j, i + j - 1, self.get_str(s1, i - 1), \
                    self.get_str(s2, j - 1), self.get_str(s3, i + j - 1)

        return mtx[m - 1][n - 1]


# print Solution().isInterleave("XXY", "XXZ", "XXZXXXY")
print Solution().isInterleave("XY", "WZ", "WZXY")
# print Solution().isInterleave("XY", "X", "XXY")
# print Solution().isInterleave("YX", "X", "XXY")
# print Solution().isInterleave("XXY", "XXZ", "XXXXZY")
# print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
# print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")
