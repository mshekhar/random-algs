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

    def search(self, word, remaining_changes=1, start=0, trie_node=None):
        curr = trie_node or self.trie_root
        c = start
        # if word[:start] == 'hh':
        #     import pdb
        #     pdb.set_trace()
        if c == len(word) - 1:
            if remaining_changes > 0:
                for i, next_trie_node in enumerate(curr.next_radix):
                    if i == ord(word[c]) - ord('a'):
                        continue
                    if bool(next_trie_node) and next_trie_node.is_word:
                        return True
                return False
            else:
                while curr and c < len(word):
                    char_idx = ord(word[c]) - ord('a')
                    curr = curr.next_radix[char_idx]
                    c += 1
                return bool(curr) and curr.is_word

        if remaining_changes > 0:
            for i, next_trie_node in enumerate(curr.next_radix):
                if i == ord(word[c]) - ord('a'):
                    continue
                if next_trie_node and self.search(word, remaining_changes - 1, c + 1, next_trie_node):
                    return True

            char_idx = ord(word[c]) - ord('a')
            next_trie_node = curr.next_radix[char_idx]
            if next_trie_node and self.search(word, remaining_changes, c + 1, next_trie_node):
                return True
            return False
        else:
            while curr and c < len(word):
                char_idx = ord(word[c]) - ord('a')
                curr = curr.next_radix[char_idx]
                c += 1
            return bool(curr) and curr.is_word


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.trie.insert(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
# obj.buildDict(["hel"])
# print obj.search("hel")
# print obj.search("hhl")
obj.buildDict(["hello", "leetcode"])
print obj.search("hello")
print obj.search("hhllo")
print obj.search("hell")
print obj.search("leetcoded")
