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

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.trie_root
        c = 0
        while curr and c < len(word):
            char_idx = ord(word[c]) - ord('a')
            curr = curr.next_radix[char_idx]
            if curr and curr.is_word:
                return curr.word
            c += 1
        return word


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)

        new_sentence = []
        for word in sentence.split(" "):
            new_sentence.append(trie.search(word))
        return " ".join(new_sentence)


print Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
