class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = {}
        for i in dictionary:
            abv = i[0] + str(len(i) - 2) + i[-1] if len(i) > 2 else i
            if abv in self.d and self.d[abv] != i:
                self.d[abv] = -1
            else:
                self.d[abv] = i
        print self.d

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # print word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word
        abv = (word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word)
        if (abv not in self.d) or (abv in self.d and self.d[abv] == word):
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["deer", "door", "cake", "card"])
print obj.isUnique("dear")
print obj.isUnique("cart")
print obj.isUnique("cane")
print obj.isUnique("make")

obj = ValidWordAbbr(["hello"])
print obj.isUnique("hello")

obj = ValidWordAbbr(["a", "a"])
print obj.isUnique("a")
# param_1 = obj.isUnique(word)
