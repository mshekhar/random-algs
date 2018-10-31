class Solution(object):
    def is_palindrome(self, word, i, j):
        while i < j:
            if word[i] == word[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def backtrack(self, word, res, ele_list, word_start):
        if word_start == len(word):
            res.append(ele_list[:])
        i = word_start
        while i < len(word):
            if self.is_palindrome(word, word_start, i):
                ele_list.append(word[word_start:i + 1])
                self.backtrack(word, res, ele_list, i + 1)
                ele_list.pop()
            i += 1

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.backtrack(s, res, [], 0)
        return res


print Solution().partition("aab")
