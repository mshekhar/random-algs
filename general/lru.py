class Node(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next_obj = None
        self.prev_obj = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.dll_start = None
        self.dll_end = None

    def print_dll(self):
        node = self.dll_start
        s = ''
        while node.next_obj is not None:
            s += str(node.data) + '->'
            node = node.next_obj
        s += str(node.data) + '->'
        return s

    def move_ele_to_head(self, node):
        if node.prev_obj and node.next_obj:
            node.prev_obj.next_obj = node.next_obj
            node.next_obj.prev_obj = node.prev_obj
        elif node.prev_obj:
            node.prev_obj.next_obj = node.next_obj
            self.dll_end = node.prev_obj
        elif node.next_obj:
            return
        elif not node.prev_obj and not node.next_obj and node.data and node.key and self.dll_start:
            # print 'first ele ', node.prev_obj, node.next_obj, node.data, node.key, self.dll_start, self.dll_start.key
            node.next_obj = self.dll_start
            self.dll_start.prev_obj = node

        # else:
        #     raise Exception('Bad Node %r %r' % (repr(node.key), repr(node.data)))
        node.prev_obj = None
        node.next_obj = self.dll_start
        if self.dll_start:
            self.dll_start.prev_obj = node
        self.dll_start = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        if node:
            self.move_ele_to_head(node)
            # print self.print_dll(), self.cache, self.dll_start.key, self.dll_end.key
            return node.data
        # print self.print_dll(), cache.cache, self.dll_start.key, self.dll_end.key
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)
        if not node:
            node = Node(key=key, data=value)
            if len(self.cache) == self.capacity:
                # print self.print_dll(), self.cache, self.dll_start.key, self.dll_end.key
                # print 'dll_end  ', self.dll_end.data, self.dll_start.data, self.dll_start.next_obj, self.dll_end.prev_obj
                node_to_remove = self.dll_end
                self.dll_end = node_to_remove.prev_obj
                self.dll_end.next_obj = None
                # print 'setting dll_end to ', node_to_remove.prev_obj
                self.cache.pop(node_to_remove.key)
        elif value != node.data:
            node.data = value

        self.cache[key] = node
        self.move_ele_to_head(node)
        if self.dll_end is None:
            self.dll_end = node
            # print self.print_dll(), self.cache, self.dll_start.key, self.dll_end.key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# try:
#     # import pdb
#     #
#     # pdb.set_trace()
#     cache = LRUCache(3)
#     cache.put(1, 1)
#     cache.put(2, 2)
#     cache.put(3, 3)
#     cache.put(4, 4)
#     print cache.print_dll(), cache.cache, cache.dll_start.key, cache.dll_end.key
#     print cache.get(4)
#     print cache.get(3)
#     print cache.get(2)
#     print cache.get(1)
#     print cache.print_dll(), cache.cache, cache.dll_start.key, cache.dll_end.key
#     cache.put(5, 5)
#     print cache.print_dll(), cache.cache, cache.dll_start.key, cache.dll_end.key
#     print cache.get(1)
#     print cache.get(2)
#     print cache.get(3)
#     print cache.print_dll(), cache.cache, cache.dll_start.key, cache.dll_end.key
#     print cache.get(4)
#     print cache.get(5)
#     print cache.print_dll(), cache.cache, cache.dll_start.key, cache.dll_end.key
# except Exception, e:
#     import time
#
#     time.sleep(.5)
#     raise
