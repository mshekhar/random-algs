import string


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S or not words:
            return 0
        letter_map = {k: [] for k in string.lowercase}
        for word in words:
            letter_map[word[0]].append((word, 0))
        res = 0
        for i in S:
            added_words = []
            while letter_map[i]:
                word, idx = letter_map[i].pop()
                if idx + 1 < len(word):
                    if word[idx + 1] == i:
                        added_words.append((word, idx + 1))
                    else:
                        letter_map[word[idx + 1]].append((word, idx + 1))
                else:
                    res += 1
            letter_map[i] = added_words

        return res


print Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
