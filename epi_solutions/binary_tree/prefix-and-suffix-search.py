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
        self.is_reverse = False

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
                if self.is_reverse:
                    curr.word = word[::-1]
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


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        self.suffix_trie.is_reverse = True
        for c, word in enumerate(words):
            self.prefix_trie.insert(word, c)
            self.suffix_trie.insert(word[::-1], c)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        prefix_words = self.prefix_trie.get_all_words_by_prefix(prefix)
        suffix_words = self.suffix_trie.get_all_words_by_prefix(suffix[::-1])
        matching_words = sorted(prefix_words & suffix_words, key=lambda x: x[1], reverse=True)
        if matching_words:
            return matching_words[0][1]
        return -1

    @classmethod
    def runner(cls, init_list, call_list):
        import time
        t = time.time()
        obj = WordFilter(init_list)
        for i in call_list:
            print obj.f(*i)
        print time.time() - t


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(["apple", "bale"])
# print obj.f("a", "e")
# print obj.f("", "")
# print obj.f("b", "e")
# print obj.f("c", "")
WordFilter.runner(
    ["hwxekxrbst", "xtmkmgencg", "odsdjhjjkk", "wxaxuswqxc", "rmurhkmuze", "kgphhwokcm", "lvoapqeppp", "pcpsdhfcsh",
     "alztysttkq", "nhfttbpzwf"], [
        ["alztysttkq", "tkq"],
        ["al", "ysttkq"],
        ["rmurhkmuze", "rmurhkmuze"],
        ["kg", "kgphhwokcm"],
        ["nhfttbpzwf", "fttbpzwf"],
        ["nhfttbpzwf", "fttbpzwf"],
        ["xtmkmgencg", "mkmgencg"],
        ["kgph", "hhwokcm"],
        ["", "tysttkq"],
        ["alztystt", ""]])
