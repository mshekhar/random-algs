class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = version1.split(".")
        v2 = version2.split(".")
        i = 0
        j = 0
        while i < len(v1) and j < len(v2):
            if float(v1[i]) > float(v2[i]):
                return 1
            elif float(v1[i]) == float(v2[i]):
                i += 1
                j += 1
            else:
                return -1
        # print 'e ', i, len(v1), j, len(v2)
        if i < len(v1):
            # print 'e ', i, len(v1), j, len(v2),
            while i < len(v1) and float(v1[i]) == 0:
                i += 1
            if i < len(v1):
                return 1
        elif j < len(v2):
            while j < len(v2) and float(v2[j]) == 0:
                j += 1
            if j < len(v2):
                return -1
        return 0


print Solution().compareVersion("0.1", "1.1")
print Solution().compareVersion("1.0.1", "1")
print Solution().compareVersion("7.5.2.4", "7.5.3")
print Solution().compareVersion("7.5.2.4", "7.5.2.4.5")
print Solution().compareVersion("7.5.2.4", "7.5.2.4")
print Solution().compareVersion("1.0", "1")
print Solution().compareVersion("1", "1.0")
