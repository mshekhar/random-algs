import collections


class FreqStack(object):

    def __init__(self):
        self.item_list = collections.defaultdict(list)
        self.freq = collections.Counter()
        self.max_frequency = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.freq[x] += 1
        self.item_list[self.freq[x]].append(x)
        self.max_frequency = max(self.max_frequency, self.freq[x])

    def pop(self):
        """
        :rtype: int
        """
        ret_val = self.item_list[self.max_frequency].pop()
        self.freq[ret_val] -= 1
        if not self.item_list[self.max_frequency]:
            self.max_frequency -= 1
        return ret_val


# Your FreqStack object will be instantiated and called as such:
def generic_runner(oper, val):
    try:
        obj = FreqStack()
        oper = oper[1:]
        val = val[1:]
        for op, v in zip(oper[1:], val[1:]):
            if v:
                res = getattr(obj, op)(v[0])
            else:
                res = getattr(obj, op)()
            print op, v, res
    except:
        import time
        time.sleep(0.2)
        print op, v
        raise


generic_runner(["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop","pop"],
               [[], [5], [7], [5], [7], [4], [5], [], [], [], [], []])
# param_2 = obj.pop()
