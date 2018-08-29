class Solution(object):
    def is_cts_char(self, x1, x2):
        # print 'is_cts_char', x1, x2
        if ord(x2) - ord(x1) == 1:
            return True
        elif ord(x1) - ord(x2) == 25:
            return True
        return False

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """

        max_len_dp = []
        uniq_dp = {}
        if not p:
            return 0
        if ord('a') <= ord(p[0]) <= ord('z'):
            max_len_dp.append(1)
            uniq_dp[p[0]] = 1
        else:
            max_len_dp.append(0)
            uniq_dp[p[0]] = 0

        # print p[0], p
        # print max_len_dp

        for c in range(1, len(p)):
            if ord('a') <= ord(p[c]) <= ord('z'):
                if self.is_cts_char(p[c - 1], p[c]):
                    # print 'adding cts ', max_len_dp[-1], max_len_dp[-1] + 1
                    max_len_dp.append(max_len_dp[-1] + 1)
                else:
                    max_len_dp.append(1)
            else:
                max_len_dp.append(0)
            uniq_dp[p[c]] = max(uniq_dp.get(p[c], 0), max_len_dp[c])
            # print p[c], p
            # print max_len_dp
        return sum(uniq_dp.values())


print Solution().findSubstringInWraproundString("zab")
print Solution().findSubstringInWraproundString("cac")
print Solution().findSubstringInWraproundString("a")
print Solution().findSubstringInWraproundString("")
print Solution().findSubstringInWraproundString("1")
print Solution().findSubstringInWraproundString("1zab")
