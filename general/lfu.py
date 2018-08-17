from collections import OrderedDict


class LFUItem(object):
    def __init__(self):
        self.key = None
        self.val = None
        self.freq = None

    def __str__(self):
        return str(self.key) + "__" + str(self.val) + "__" + str(self.freq)

    def __repr__(self):
        return str(self.key) + "__" + str(self.val) + "__" + str(self.freq)


class FreqDLLNode(object):
    def __init__(self):
        self.freq = None
        self.freq_list = OrderedDict()
        self.next = None
        self.prev = None

    def add_item(self, ele):
        self.freq_list[ele.key] = ele

    def pop_item(self, key=None):
        if key and key in self.freq_list:
            return self.freq_list.pop(key)
        else:
            return self.freq_list.popitem(last=False)[1]

    @classmethod
    def print_ll(cls, head):
        arr = []
        curr = head
        while curr:
            arr.append((curr.freq, curr.freq_list))
            if curr.next:
                curr = curr.next
            else:
                break
        return arr

    def __repr__(self):
        return str(self.freq) + "__" + str(self.freq_list)


class LFUFrequencyDLLManager(object):
    def __init__(self):
        self.dll_lookup_map = {}
        self.freq_dll_head = None
        self.freq_dll_curr = None

    def add_new_ele(self, ele):
        freq_node = self.dll_lookup_map.get(ele.freq)
        if freq_node:
            freq_node.freq_list[ele.key] = ele
        else:
            freq_dll_node = FreqDLLNode()
            freq_dll_node.freq = ele.freq
            freq_dll_node.freq_list[ele.key] = ele
            self.dll_lookup_map[ele.freq] = freq_dll_node
            freq_dll_curr = self.freq_dll_head

            while freq_dll_curr and freq_dll_curr.freq < ele.freq:
                if not freq_dll_curr.next:
                    freq_dll_curr.next = freq_dll_node
                    freq_dll_node.prev = freq_dll_curr
                    return
                freq_dll_curr = freq_dll_curr.next

            if freq_dll_curr:
                if freq_dll_curr.prev:
                    freq_dll_curr.prev.next = freq_dll_node
                    freq_dll_node.prev = freq_dll_curr.prev

                    freq_dll_curr.prev = freq_dll_node

                    freq_dll_node.next = freq_dll_curr
                else:
                    freq_dll_node.next = freq_dll_curr
                    freq_dll_curr.prev = freq_dll_node

                    self.freq_dll_head = freq_dll_node
            else:
                self.freq_dll_head = freq_dll_node
        # print 'add_item', self.dll_lookup_map, self.freq_dll_head, self.freq_dll_head.prev, self.freq_dll_head.next

    def check_and_delete_empty_node(self, freq_node):
        if not freq_node.freq_list:
            if freq_node.prev and freq_node.next:
                freq_node.prev.next = freq_node.next
                freq_node.next.prev = freq_node.prev
            elif freq_node.prev:
                freq_node.prev.next = freq_node.next
            elif freq_node.next:
                freq_node.next.prev = freq_node.prev
                self.freq_dll_head = freq_node.next
            else:
                self.freq_dll_head = None
            self.dll_lookup_map.pop(freq_node.freq)

    def remove_ele(self, ele):
        freq_node = self.dll_lookup_map.get(ele.freq)
        if freq_node and ele.key in freq_node.freq_list:
            freq_node.pop_item(key=ele.key)
            self.check_and_delete_empty_node(freq_node)
        # print 'remove_ele', self.dll_lookup_map, self.freq_dll_head, self.freq_dll_head.prev, self.freq_dll_head.next

    def incr_freq_for_ele(self, ele):
        self.remove_ele(ele)
        ele.freq += 1
        self.add_new_ele(ele)

    def pop_least_freq_ele(self):
        popped_ele = None
        if self.freq_dll_head:
            popped_ele = self.freq_dll_head.pop_item()
            # print 'popped_ele', popped_ele
            freq_node = self.dll_lookup_map.get(popped_ele.freq)
            if freq_node:
                self.check_and_delete_empty_node(freq_node)
        # print 'pop_least_freq_ele', self.dll_lookup_map, self.freq_dll_head, self.freq_dll_head.prev, self.freq_dll_head.next
        return popped_ele


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys_map = {}
        self.capacity = capacity
        self.dll_manager = LFUFrequencyDLLManager()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ret_val = self.keys_map.get(key)
        if not ret_val:
            return -1
        self.dll_manager.incr_freq_for_ele(ret_val)
        return ret_val.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.capacity:
            return
        if key in self.keys_map:
            self.keys_map[key].val = value
            self.dll_manager.incr_freq_for_ele(self.keys_map[key])
            return

        ele = LFUItem()
        ele.key = key
        ele.val = value
        ele.freq = 0
        if len(self.keys_map) >= self.capacity:
            popped_ele = self.dll_manager.pop_least_freq_ele()
            # print 'popped ele', popped_ele, self.capacity
            self.keys_map.pop(popped_ele.key)
        # print 'adding key to map', key, ele, len(self.keys_map), self.capacity
        self.keys_map[key] = ele
        self.dll_manager.add_new_ele(ele)


def test1():
    # Your LFUCache object will be instantiated and called as such:
    cache = LFUCache(2)

    print cache.put(1, 1), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.put(2, 2), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.get(1), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # returns 1
    print cache.put(3, 3), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # evicts key 2
    print cache.get(2), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # returns -1 (not found)
    print cache.get(3), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # returns 3.
    print cache.put(4, 4), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # evicts key 1.
    print cache.get(1), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # returns -1 (not found)
    print cache.get(3), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # returns 3
    print cache.get(4), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    # returns 4


def test2():
    # Your LFUCache object will be instantiated and called as such:
    cache = LFUCache(0)
    print cache.put(0, 0), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.get(0), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map


def test3():
    # Your LFUCache object will be instantiated and called as such:
    cache = LFUCache(2)

    print cache.get(2), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.put(2, 6), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.get(1), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.put(1, 5), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.put(1, 2), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.get(1), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
    print cache.get(2), FreqDLLNode.print_ll(cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map


def generic_runner(oper, val, expected):
    cache = LFUCache(val[0][0])
    print cache.__dict__
    c = 1
    for op, v in zip(oper[1:], val[1:]):
        # print 'add_item ', op, v
        # if op == 'put' and v[0] == 3 and v[1] == 27:
        #     import pdb
        #     pdb.set_trace()
        res = getattr(cache, op)(*v)
        print op, v, expected[c], res, len(cache.keys_map), FreqDLLNode.print_ll(
            cache.dll_manager.freq_dll_head), cache.dll_manager.dll_lookup_map
        c += 1


generic_runner(
    ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"],
    [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2],
     [3], [5, 25], [8], [9, 22], [5, 5], [1, 30],
     [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10],
     [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1],
     [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27],
     [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7],
     [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
     [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30],
     [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28],
     [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9],
     [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19],
     [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]],
    [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1, 12, None,
     None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None, None, 18, None,
     None, None, None, 14, None, None, 18, None, None, 11, None, None, None, None, None, 18, None, None, -1, None, 4, 29,
     30, None, 12, 11, None, None, None, None, 29, None, None, None, None, 17, -1, 18, None, None, None, -1, None, None,
     None, 20, None, None, None, 29, 18, 18, None, None, None, None, 20, None, None, None, None, None, None, None])
