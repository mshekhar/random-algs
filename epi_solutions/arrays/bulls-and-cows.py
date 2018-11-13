import collections


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        a = sum(map(lambda x, y: bool(x == y), secret, guess))
        b = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (a, sum(b.values()) - a)
