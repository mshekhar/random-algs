# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# if not single_digit:
#     all_single_possible[c] = False
# else:
#     all_single_possible[c] = all_single_possible[c - 1] and all_single_possible[c]
#     if c - 1 >= 0 and num_decodings[c - 1] > 0:
#         num_decodings[c] = num_decodings[c - 1]
#
# if c - 1 >= 0:
#     double_digit = self.get_decoding_count(s[c - 1] + i)
#     if double_digit:
#         print s[c - 1] + i, double_digit, num_decodings[c - 2] + int(all_single_possible[c - 2])
#         if c - 2 >= 0 and num_decodings[c - 2] + int(all_single_possible[c - 2]) > 0:
#             num_decodings[c] += num_decodings[c - 2] + 1
#         elif c == 1:
#             num_decodings[c] += 1


class Solution(object):
    def get_decoding_count(self, s):
        if not s.startswith('0') and 1 <= int(s) <= 26:
            return 1
        return 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_decodings = [0] * len(s)
        all_single_possible = True

        for c, i in enumerate(s):
            single_digit = self.get_decoding_count(i)
            double_digit = 0
            if c - 1 >= 0:
                double_digit = self.get_decoding_count(s[c - 1] + i)
            if not single_digit:
                all_single_possible = False

            if single_digit + double_digit > 0:
                if single_digit:
                    num_decodings[c] = num_decodings[c - 1]
                if all_single_possible and not num_decodings[c]:
                    num_decodings[c] = 1
                if double_digit:
                    if c - 2 >= 0 and num_decodings[c - 2] > 0:
                        num_decodings[c] += num_decodings[c - 2]
                    elif c == 1:
                        num_decodings[c] += 1

        # add one for all single decodings
        # print num_decodings, all_single_possible
        return num_decodings[-1]


print Solution().numDecodings("12"), 2
print Solution().numDecodings("226"), 3
print Solution().numDecodings("10"), 1
print Solution().numDecodings("103"), 1
print Solution().numDecodings("1032"), 1
print Solution().numDecodings("10323"), 1
print Solution().numDecodings("012"), 0
print Solution().numDecodings("110"), 1
print Solution().numDecodings("1212"), 5
# 1 2 1
# 12 1
# 1 21
#
# 1 2 1 2
#
# 12 1 2
# 12 12
#
# 1 21 2
# 1 2 12


# for i in ["0", "10", "10", "103", "1032", "10323"]:
#     print(Solution().numDecodings(i))
