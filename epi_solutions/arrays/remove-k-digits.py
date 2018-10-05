class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st = []
        for n in num:
            while st and st[-1] > n and k > 0:
                st.pop()
                k -= 1
            st.append(n)

        # print 'f ', st, k
        while st and k > 0:
            st.pop()
            k -= 1
        res = "".join(st).lstrip('0')
        return res if res else '0'


print Solution().removeKdigits("1432219", 3)
print Solution().removeKdigits("10200", 1)
print Solution().removeKdigits("10", 2)
print Solution().removeKdigits("112", 1)
