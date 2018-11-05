import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ele_as_list = []
        self.ele_idx_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ele_idx_map:
            return False
        self.ele_as_list.append(val)
        self.ele_idx_map[val] = len(self.ele_as_list) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ele_idx_map:
            return False
        ele_counter = self.ele_idx_map.pop(val)
        if ele_counter == len(self.ele_as_list) - 1:
            self.ele_as_list.pop()
        else:
            self.ele_as_list[ele_counter] = self.ele_as_list.pop()
            self.ele_idx_map[self.ele_as_list[ele_counter]] = ele_counter
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.ele_as_list[random.randint(0, len(self.ele_as_list) - 1)]

    @classmethod
    def generic_runner(cls, oper, val, expected):
        obj = RandomizedSet()
        c = 1
        for op, v in zip(oper[1:], val[1:]):
            res = getattr(obj, op)(*v)
            print op, v, expected[c], res, expected[c] == res
            c += 1


null = None
true = True
false = False
print RandomizedSet.generic_runner(
    ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
    [[], [1], [2], [2], [], [1], [2], []],
    [null, true, false, true, 2, true, false, 2])
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
