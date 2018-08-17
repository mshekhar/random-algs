class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList_map = {w: False for w in wordList}
        for word in wordList_map:
            count = sum(1 for a, b in zip(beginWord, wordList_map) if a != b)
            if count == 1:
                wordList_map[word] = True

