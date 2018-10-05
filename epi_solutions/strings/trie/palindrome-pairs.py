class TrieNode(object):
    def __init__(self):
        self.word_idx = None
        self.next_radix = [None] * 26
        self.matching_suffix_indices = []


class TrieHelper(object):
    @classmethod
    def is_palindrome(cls, word, i, j):
        while i < j:
            if word[i] == word[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    @classmethod
    def add_word(cls, word, word_idx, root):
        curr = root
        c = len(word) - 1
        while c >= 0:
            char = word[c]
            char_idx = ord(char) - ord('a')
            curr.next_radix[char_idx] = curr.next_radix[char_idx] or TrieNode()
            if cls.is_palindrome(word, 0, c):
                curr.next_radix[char_idx].matching_suffix_indices.append(word_idx)
            curr = curr.next_radix[char_idx]
            c -= 1
        curr.word_idx = word_idx
        curr.matching_suffix_indices.append(word_idx)

    @classmethod
    def search(cls, word, word_idx, res, root):
        curr = root
        for c, char in enumerate(word):
            if curr.word_idx >= 0 and curr.word_idx != word_idx and cls.is_palindrome(word, c, len(word) - 1):
                res.append([word_idx, curr.word_idx])

            curr = curr.next_radix[ord(char) - ord('a')]
            if not curr:
                return
        for idx in curr.matching_suffix_indices:
            if idx == word_idx:
                continue
            res.append([word_idx, idx])


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        trie_root = TrieNode()
        for i, word in enumerate(words):
            TrieHelper.add_word(word, i, trie_root)
        for i, word in enumerate(words):
            TrieHelper.search(word, i, res, trie_root)
        return res


print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
