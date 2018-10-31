class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.word = None
        self.next_radix = [None] * 26

    def __str__(self):
        return str(id(self)) + "_" + str(self.word)


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
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

    def is_valid_prefix(self, prefix):
        curr = self.trie_root
        c = 0
        while curr and c < len(prefix):
            char_idx = ord(prefix[c]) - ord('a')
            curr = curr.next_radix[char_idx]
            c += 1
        return curr

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie_node = self.is_valid_prefix(word)
        return bool(trie_node) and trie_node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return bool(self.is_valid_prefix(prefix))


# Your Trie object will be instantiated and called as such:
obj = Trie()
print obj.insert("apple")
print obj.search("apple")
print obj.search("app")
print obj.startsWith("app")
print obj.insert("app")
print obj.search("app")

# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
