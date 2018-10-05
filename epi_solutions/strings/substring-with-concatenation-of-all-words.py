class Solution(object):
    def helper(self, s, start, len_word, len_match, freq, ans):
        word_matches = {}
        i = start
        sol_start = i
        while i + len_word <= len(s):
            word = s[i:i + len_word]
            i += len_word
            if word not in freq:
                sol_start = i
                word_matches.clear()
                continue
            if word not in word_matches:
                word_matches[word] = 0
            word_matches[word] += 1
            while word_matches[word] > freq[word]:
                word_matches[s[sol_start:sol_start + len_word]] -= 1
                sol_start += len_word
            if i - sol_start == len_match:
                ans.append(sol_start)
            # print i, word, word_matches

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        len_word = len(words[0])
        len_match = len_word * len(words)

        freq = {}
        for i in words:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        ans = []
        for start in xrange(min(len_word, len(s) - len_match + 1)):
            self.helper(s, start, len_word, len_match, freq, ans)
        return ans


print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
print Solution().findSubstring("wordgoodstudentgoodword", ["word", "student"])
