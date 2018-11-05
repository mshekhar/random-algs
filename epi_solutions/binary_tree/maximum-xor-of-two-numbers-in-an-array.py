class TrieNode(object):
    def __init__(self):
        self.next_radix = [None, None]

    def __str__(self):
        return str(id(self)) + "_" + str(self.next_radix)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()

    def insert(self, word):
        curr = self.trie_root
        c = 31
        while c >= 0:
            cur_bit = (word >> c) & 1
            curr.next_radix[cur_bit] = curr.next_radix[cur_bit] or TrieNode()
            curr = curr.next_radix[cur_bit]
            c -= 1
        # print 'inserted', word, weight, self.trie_root

    def get_xor_res(self, word):
        curr = self.trie_root
        xor_res = 0
        c = 31
        while c >= 0:
            cur_bit = (word >> c) & 1
            if curr.next_radix[cur_bit ^ 1]:
                xor_res += 1 << c
                curr = curr.next_radix[cur_bit ^ 1]
            else:
                curr = curr.next_radix[cur_bit]
            c -= 1
        return xor_res


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = Trie()
        for i in nums:
            trie.insert(i)

        res = float('-inf')
        for i in nums:
            res = max(res, trie.get_xor_res(i))

        return res


print Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
