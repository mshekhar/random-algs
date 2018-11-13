import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        counter_s1 = collections.Counter(s1)
        counter_s2 = collections.Counter(s2[:len(s1)])
        # print counter_s1, counter_s2, s1, s2[:len(s1)]
        if counter_s1 == counter_s2:
            return True

        i = 0
        j = len(s1)

        while j < len(s2):
            counter_s2[s2[i]] -= 1
            if counter_s2[s2[i]] == 0:
                counter_s2.pop(s2[i])
            i += 1
            counter_s2[s2[j]] += 1
            j += 1
            if counter_s1 == counter_s2:
                return True
        return False


print Solution().checkInclusion("hello", "ooolleoooleh")

# print Solution().checkInclusion("abcdxabcde", "abcdeabcdx")
# print Solution().checkInclusion(s1="ab", s2="eidbaooo")
# print Solution().checkInclusion(s1="ab", s2="eidboaoo")
