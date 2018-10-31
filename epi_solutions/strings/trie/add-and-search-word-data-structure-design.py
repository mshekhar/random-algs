class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.word = None
        self.next_radix = [None] * 26

    def __str__(self):
        return str(id(self)) + "_" + str(self.word)


class Trie(object):

    def __init__(self):
        self.trie_root = TrieNode()

    def insert(self, word):
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

    def search(self, word, start=0, trie_node=None):
        curr = trie_node or self.trie_root
        c = start
        while curr and c < len(word):
            if word[c] == '.':
                for next_trie_node in curr.next_radix:
                    if next_trie_node and self.search(word, c + 1, next_trie_node):
                        return True
                return False
            else:
                char_idx = ord(word[c]) - ord('a')
                curr = curr.next_radix[char_idx]
            c += 1
        return bool(curr) and curr.is_word


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        return self.trie.search(word)
