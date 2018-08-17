import random
from bisect import insort_left


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        initially_present = val not in self.counter
        if initially_present:
            self.counter[val] = []
        self.counter[val].append(len(self.arr))
        self.arr.append(val)
        return initially_present

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.counter:
            return False
        last_inserted_pos = self.counter[val].pop()
        last_ele = self.arr.pop()

        if not self.counter[val]:
            self.counter.pop(val)

        if last_ele == val:
            return True
        # print 'remove start', last_inserted_pos, last_ele, self.counter[last_ele], self.counter[val]
        self.arr[last_inserted_pos] = last_ele
        self.counter[last_ele].pop()
        insort_left(self.counter[last_ele], last_inserted_pos)
        # print 'remove end', last_inserted_pos, last_ele, self.counter[last_ele], self.counter[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.arr)
