class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [None] * k
        self.front = self.rear = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.front == -1:
            self.front = 0
        if self.rear == -1 or self.rear == len(self.queue) - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        if self.front == len(self.queue) - 1:
            self.front = 0
        else:
            self.front += 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.front == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.front == 0 and self.rear == len(self.queue) - 1) or self.front - 1 == self.rear

    @classmethod
    def generic_runner(cls, oper, val, expected):
        obj = MyCircularQueue(*val[0])
        c = 1
        for op, v in zip(oper[1:], val[1:]):
            res = getattr(obj, op)(*v)
            print op, v, expected[c], res, obj.queue, obj.front, obj.rear, expected[c] == res
            c += 1


null = None
true = True
false = False
MyCircularQueue.generic_runner(
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
     "Rear", "isFull", "deQueue", "enQueue", "Rear", "isFull", "deQueue", "deQueue", "deQueue", "deQueue"],
    [[3], [1], [2], [3], [4], [], [], [], [4], [], [], [], [], [], []],
    [null, true, true, true, false, 3, true, true, true, 4, true, true, true, true, false])
