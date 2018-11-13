class Solution(object):
    def helper(self, s, start):
        res = []
        curr_num = 0
        curr_str = []
        i = start

        while i[0] < len(s) and ord('0') <= ord(s[i[0]]) <= ord('9'):
            curr_num = curr_num * 10 + int(s[i[0]])
            i[0] += 1
        # skip [ char and begin str construction
        i[0] += 1
        while i[0] < len(s) and s[i[0]] != ']':
            if ord('0') <= ord(s[i[0]]) <= ord('9'):
                curr_str.extend(self.helper(s, i))
                continue
            curr_str.append(s[i[0]])
            i[0] += 1
        # print curr_str, curr_num
        res.extend(curr_str * curr_num)
        i[0] += 1
        return res

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = [0]
        while i[0] < len(s):
            if ord('0') <= ord(s[i[0]]) <= ord('9'):
                res.extend(self.helper(s, i))
            else:
                res.append(s[i[0]])
                i[0] += 1
        return "".join(res)


print Solution().decodeString("3[a]2[bc]")
print Solution().decodeString("3[a2[c]]")
print Solution().decodeString("2[abc]3[cd]ef")
print Solution().decodeString("")
print Solution().decodeString("2[a]")
print Solution().decodeString("2[abc]3[cd]ef")
