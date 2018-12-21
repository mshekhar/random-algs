class TrieNode(object):
    def __init__(self):
        self.next_radix = [None for _ in xrange(26)]
        self.is_word = False
        self.frequency = 0


class Solution():
    def __init__(self):
        self.root = TrieNode()

    def insert_to_trie(self, word, start, end, m):
        distinct_chars = set()
        parent = self.root
        i = start
        while i < end:
            c = word[i]
            distinct_chars.add(word)
            if len(distinct_chars) > m:
                return -1
            idx = ord(c) - ord('a')
            if parent.next_radix[idx] is None:
                parent.next_radix[idx] = TrieNode()
            parent = parent.next_radix[idx]
            i += 1

        if parent.is_word:
            parent.frequency += 1
        else:
            parent.is_word = True
            parent.frequency = 1

        return parent.frequency

    def getMaxOccurrences(self, s, minLength, maxLength, maxUnique):
        if not s or minLength < 0 or maxLength < 0 or maxUnique <= 0:
            return 0

        max_freq = 1
        for i in xrange(len(s)):
            for j in xrange(i + minLength, min(i + maxLength, len(s)) + 1):
                curr_freq = self.insert_to_trie(s, i, j, maxUnique)
                # print s[i: j]
                if curr_freq == -1:
                    break
                max_freq = max(curr_freq, max_freq)
        return max_freq

    def getMaxOccurrences2(self, s, minLength, maxLength, maxUnique):
        counter = {}
        not_unique = set()
        max_freq = 1
        for i in xrange(len(s)):
            for j in xrange(i + minLength, min(i + maxLength, len(s)) + 1):
                sub_str = s[i:j]
                if sub_str in not_unique:
                    break
                if len(set(sub_str)) <= maxUnique:
                    if sub_str not in counter:
                        counter[sub_str] = 0
                    counter[sub_str] += 1
                    max_freq = max(max_freq, counter[sub_str])
                else:
                    not_unique.add(sub_str)
                    break
        return max_freq


def getMaxOccurrences(s, minLength, maxLength, maxUnique):
    return Solution().getMaxOccurrences2(s, minLength, maxLength, maxUnique)


print getMaxOccurrences("abcde", 2, 4, 26)
print getMaxOccurrences("ababab", 2, 3, 4)
