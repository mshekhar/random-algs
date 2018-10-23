class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.word = None
        self.next_radix = [None] * 26

    def __str__(self):
        return str(id(self)) + "_" + str(self.word)


class TrieHelper(object):
    def __init__(self):
        self.trie_root = TrieNode()

    def add_word(self, word):
        curr = self.trie_root
        c = 0
        while c < len(word):
            char = word[c]
            char_idx = ord(char) - ord('a')
            curr.next_radix[char_idx] = curr.next_radix[char_idx] or TrieNode()
            curr = curr.next_radix[char_idx]
            if c == len(word) - 1:
                curr.is_word = True
                curr.word = word
            c += 1

    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def is_valid_prefix(self, prefix):
        curr = self.trie_root
        c = 0
        while curr and c < len(prefix):
            char_idx = ord(prefix[c]) - ord('a')
            curr = curr.next_radix[char_idx]
            c += 1
        return curr

    def is_valid_word(self, word):
        trie_node = self.is_valid_prefix(word)
        return bool(trie_node) and trie_node.is_word


class Solution(object):
    def helper(self, row, col, board, m, n, matched_words, trie_node):
        if row < 0 or col < 0 or row >= m or col >= n:
            return
        next_char = board[row][col]
        if next_char == '!' or trie_node.next_radix[ord(next_char) - ord('a')] is None:
            return
        next_trie_node = trie_node.next_radix[ord(next_char) - ord('a')]
        if next_trie_node.is_word:
            matched_words.append(next_trie_node.word)
            next_trie_node.is_word = False
        board[row][col] = '!'
        self.helper(row + 1, col, board, m, n, matched_words, next_trie_node)
        self.helper(row - 1, col, board, m, n, matched_words, next_trie_node)
        self.helper(row, col + 1, board, m, n, matched_words, next_trie_node)
        self.helper(row, col - 1, board, m, n, matched_words, next_trie_node)
        board[row][col] = next_char

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        matched_words = []
        try:
            m = len(board)
            n = len(board[0])
            if m < 1 or n < 1:
                return matched_words
        except IndexError:
            return matched_words

        t = TrieHelper()
        t.add_words(words)
        for row in xrange(m):
            for col in xrange(n):
                self.helper(row, col, board, m, n, matched_words, t.trie_root)
        return matched_words


print Solution().findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"])
