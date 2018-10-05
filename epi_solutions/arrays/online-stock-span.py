class StackItem(object):
    def __init__(self):
        self.price = None
        self.day = None

    def __str__(self):
        return str(self.price) + "__" + str(self.day)

    def __repr__(self):
        return str(self.price) + "__" + str(self.day)


class StockSpanner(object):
    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.day += 1
        while self.stack and self.stack[-1].price <= price:
            self.stack.pop()

        prev_day = self.stack[-1].day if self.stack else 0
        stack_item = StackItem()
        stack_item.price = price
        stack_item.day = self.day
        self.stack.append(stack_item)
        # print self.stack
        return self.day - prev_day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

def generic_runner(oper, val, expected):
    obj = StockSpanner()
    c = 1
    for op, v in zip(oper[1:], val[1:]):
        res = getattr(obj, op)(*v)
        print op, v[0], expected[c], res, expected[c] == res
        c += 1


null = None
generic_runner(["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
               [[], [100], [80], [60], [70], [60], [75], [85]],
               [null, 1, 1, 1, 2, 1, 4, 6])
generic_runner(["StockSpanner", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next"],
               [[], [28], [14], [28], [35], [46], [53], [66], [80], [87], [88]],
               [null, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10])
generic_runner(
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next", "next",
     "next", "next", "next"],
    [[], [3], [5], [8], [8], [14], [56], [25], [30], [32], [42], [43], [15], [75], [76], [81]],
    [null, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 1, 13, 14, 15])
