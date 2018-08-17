from utils.linked_lists import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.current = None

    def set_head(self, node):
        if self.head is None:
            self.head = node

    def set_tail(self, node):
        if self.tail is None or node.next_obj is None:
            self.tail = node

    def insert_node(self, node, prev=None):
        if prev is None:
            node.next_obj = None
            if self.tail is not None:
                self.tail.next_obj = node
        else:
            prev.next_obj = node
        self.set_tail(node)
        self.set_head(node)
        self.length += 1

    def insert_data(self, data):
        node = Node()
        node.data = data
        node.next_obj = None
        if self.tail:
            self.tail.next_obj = node
            self.tail = node
        else:
            self.set_tail(node)
            self.set_head(node)
        self.length += 1

    def traverse(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next_obj

    def pop(self):
        while True:
            try:
                cur = self.head
                self.head = self.head.next_obj
                yield cur
            except AttributeError:
                break
        self.tail = None

    def __str__(self):
        ll_string = ''
        for node in self.traverse():
            ll_string += repr(node.data) + '  '
            # import time
            # time.sleep(1)
            # print 'after iter ', ll_string
        return ll_string
