class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = [None] * k
        self.front = self.rear = -1

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.rear == -1:
            self.rear = 0
            self.front = 0
        elif self.front == 0:
            self.front = len(self.queue) - 1
        else:
            self.front -= 1
        self.queue[self.front] = value
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
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

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
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

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.queue[self.rear] = None
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        if self.rear == 0:
            self.rear = len(self.queue) - 1
        else:
            self.rear -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.front == -1

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return (self.front == 0 and self.rear == len(self.queue) - 1) or self.front - 1 == self.rear

    @classmethod
    def generic_runner(cls, oper, val, expected):
        obj = MyCircularDeque(*val[0])
        c = 1
        for op, v in zip(oper[1:], val[1:]):
            res = getattr(obj, op)(*v)
            print op, v, expected[c], res, obj.queue, obj.front, obj.rear, expected[c] == res
            c += 1


null = None
true = True
false = False
MyCircularDeque.generic_runner(["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
                                "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
                               [[3], [1], [2], [3], [4], [], [], [], [4], []],
                               [null, true, true, true, false, 2, true, true, true, 4])
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
