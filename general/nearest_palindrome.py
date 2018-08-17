import math
from operator import add, sub


# def increment_middle_1(self, s):
#     middle = len(s) / 2
#     middle_ele = str(int(s[middle]) + 1)[-1]
#     if len(s) % 2:
#         return s[:middle] + middle_ele + s[middle + 1:]
#     return s[:middle - 1] + middle_ele + middle_ele + s[middle + 1:]
#
#
# def decrement_middle_2(self, s):
#     middle = len(s) / 2
#     middle_ele = str(int(s[middle]) - 1)[-1]
#     if len(s) % 2:
#         return s[:middle] + middle_ele + s[middle + 1:]
#     return s[:middle - 1] + middle_ele + middle_ele + s[middle + 1:]


class Solution(object):

    def is_palindrome(self, s):
        return str(s) == str(s)[::-1]

    def is_num_all_9s(self, s):
        return all(map(lambda x: x == '9', s))

    def rotate_right_half(self, s):
        first_half = s[:len(s) / 2]
        if len(s) % 2:
            return first_half + s[len(s) / 2] + first_half[::-1]
        return first_half + first_half[::-1]

    def modify_middle(self, s, oper):
        middle = len(s) / 2
        tmp = '1'
        for i in range(middle + 1, len(s)):
            tmp += '0'
        res = str(oper(int(s), int(tmp)))
        if not self.is_palindrome(res):
            res = self.fix_modified_middle(res)
        return res

    def increment_middle(self, s):
        return self.modify_middle(s, add)

    def decrement_middle(self, s):
        import pdb
        pdb.set_trace()
        return self.modify_middle(s, sub)

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if int(n) <= 10000:
            i = 1
            while True:
                if self.is_palindrome(str(int(n) - i)):
                    return str(int(n) - i)
                elif self.is_palindrome(str(int(n) + i)):
                    return str(int(n) + i)
                i += 1
        if self.is_num_all_9s(n):
            return str(int(n) + 2)

        n_as_int = int(n)
        rotate_middle_str = self.rotate_right_half(n)
        rotate_middle = int(rotate_middle_str)

        if n_as_int < rotate_middle:
            dec_middle = int(self.decrement_middle(rotate_middle_str))
            r1 = math.fabs(rotate_middle - n_as_int)
            r2 = math.fabs(n_as_int - dec_middle)
            if r1 < r2:
                return str(rotate_middle)
            elif r1 == r2:
                return str(min(rotate_middle, dec_middle))
            return str(dec_middle)

        elif n_as_int > rotate_middle:
            inc_middle = int(self.increment_middle(rotate_middle_str))
            r1 = math.fabs(inc_middle - n_as_int)
            r2 = math.fabs(n_as_int - rotate_middle)
            if r1 < r2:
                return str(inc_middle)
            elif r1 == r2:
                return str(min(rotate_middle, inc_middle))
            return str(rotate_middle)

        else:
            dec_middle = int(self.decrement_middle(rotate_middle_str))
            inc_middle = int(self.increment_middle(rotate_middle_str))
            r1 = math.fabs(inc_middle - n_as_int)
            r2 = math.fabs(n_as_int - dec_middle)
            if r1 < r2:
                return str(inc_middle)
            if r1 == r2:
                return str(min(dec_middle, inc_middle))
            return str(dec_middle)


# print Solution().nearestPalindromic('123'), '121'
# print Solution().nearestPalindromic('919'), '909'
# print Solution().nearestPalindromic('99'), '101'
# print Solution().nearestPalindromic('199'), '202'
# print Solution().nearestPalindromic('2'), '1'
# print Solution().nearestPalindromic('9'), '8'
# print Solution().nearestPalindromic('11'), '9'
# print Solution().nearestPalindromic("10001"), "9999"
# print Solution().nearestPalindromic("11911"), "11811"
# print Solution().nearestPalindromic("11011"), "11111"
# print Solution().nearestPalindromic("99999"), "100001"
# print Solution().nearestPalindromic("1837722381"), "1837667381"

print Solution().rotate_right_half("1837722381")
print Solution().increment_middle(Solution().rotate_right_half("1837722381"))
print Solution().decrement_middle(Solution().rotate_right_half("1837722381"))
