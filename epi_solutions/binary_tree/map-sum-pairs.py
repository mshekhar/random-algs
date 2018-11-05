import Queue


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.word = None
        self.weight = None
        self.next_radix = [None] * 26

    def __str__(self):
        return str(id(self)) + "_" + str(self.word) + "_" + str(self.next_radix)


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()

    def insert(self, word, weight):
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
                curr.weight = weight
            c += 1
        # print 'inserted', word, weight, self.trie_root

    def search(self, prefix):
        curr = self.trie_root
        c = 0
        while curr and c < len(prefix):
            char_idx = ord(prefix[c]) - ord('a')
            curr = curr.next_radix[char_idx]
            c += 1
        return bool(curr) and curr.is_word

    def get_all_words_by_prefix(self, prefix):
        curr = self.trie_root
        c = 0
        while curr and c < len(prefix):
            char_idx = ord(prefix[c]) - ord('a')
            curr = curr.next_radix[char_idx]
            c += 1
        words = set()
        if not bool(curr):
            return words
        if curr.is_word:
            words.add((curr.word, curr.weight))
        q = Queue.Queue()
        q.put(curr)
        while q.qsize() > 0:
            present_node = q.get()
            if present_node.is_word:
                words.add((present_node.word, present_node.weight))
            for next_node in present_node.next_radix:
                if next_node:
                    q.put(next_node)
        return words


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prefix_trie = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.prefix_trie.insert(key, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        prefix_words = self.prefix_trie.get_all_words_by_prefix(prefix)
        if prefix_words:
            return sum(map(lambda x: x[1], prefix_words))
        return 0


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print obj.sum("ap")
obj.insert("app", 2)
print obj.sum("ap")
obj.insert("app", 7)
print obj.sum("ap")
