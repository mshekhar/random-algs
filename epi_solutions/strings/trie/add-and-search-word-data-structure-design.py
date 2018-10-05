class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.word = None
        self.next_radix = [None] * 26

    def __str__(self):
        return str(id(self)) + "_" + str(self.word)


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.trie_root
        c = 0
        while c < len(word):
            char = word[c]
            char_idx = ord(char) - ord('a')
            if c == len(word) - 1:
                curr.is_word = True
                curr.word = word
            else:
                curr.next_radix[char_idx] = curr.next_radix[char_idx] or TrieNode()
                curr = curr.next_radix[char_idx]
            c += 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        c = 0
        stack = [(self.trie_root, c)]
        while stack:
            curr, c = stack.pop()
            char = word[c]
            if word == '.a':
                print c, char, word[:c + 1], curr, curr.next_radix, stack, curr.word
            if c == len(word) - 1 and curr.is_word:
                valid_char = ord(char) - ord('a')
                if valid_char < 0:
                    if curr.next_radix.count(None) < 26:
                        return True
                elif curr.next_radix[valid_char] is not None:
                    return True
            if char != '.':
                char_idx = ord(char) - ord('a')
                if curr.next_radix[char_idx] and c + 1 < len(word):
                    stack.append((curr.next_radix[char_idx], c + 1))
            else:
                for next_radix in curr.next_radix:
                    if next_radix and c + 1 < len(word):
                        stack.append((next_radix, c + 1))
        return False


def generic_runner(oper, val, expected):
    obj = WordDictionary()
    print obj.__dict__
    c = 1
    for op, v in zip(oper[1:], val[1:]):
        # print 'add_item ', op, v
        # if op == 'put' and v[0] == 3 and v[1] == 27:
        #     import pdb
        #     pdb.set_trace()
        res = getattr(obj, op)(*v)
        print op, v, res, expected[c]
        c += 1


null = None
false = False
true = True
# generic_runner(["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
#                [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
#                [null, null, null, null, false, true, true, true])
generic_runner(
    ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search", "search",
     "search"],
    [[], ["a"], ["ab"], ["a"], ["a."], ["ab"], [".a"], [".b"], ["ab."], ["."], [".."]],
    [null, null, null, true, true, true, false, true, false, true, true])
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
