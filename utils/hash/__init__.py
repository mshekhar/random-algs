import hashlib
import time
from functools import wraps


class DynamicArrays(object):
    def __init__(self, size, default_val=None):
        self.size = size
        self.default_val = default_val
        self.array = [self.default_val] * self.size

    def set_value_at_index(self, value, index):
        if not index < self.size:
            inc_factor = 2 * self.size
            self.array.extend([self.default_val] * inc_factor)
            self.size += inc_factor
        self.array[index] = value


class ExecutionTimer(object):
    def __call__(self, func):
        @wraps(func)
        def timer(*args, **kwargs):
            a = time.time()
            return_value = func(*args, **kwargs)
            print func.__name__, ' took ', time.time() - a
            return return_value

        return timer


class CustomDict(object):
    deleted_key_dummy_name = '80f9a72e53f34e947c9f42e1a4a3a95e'

    def __init__(self):
        self.number_of_low_bits = 3
        self.element_container = self.__get_element_container()
        self.filled_slots = 0

    def __iter__(self):
        for elem in self.element_container:
            elem_hash, elem_key, elem_val = elem
            if self.__check_elem_non_empty(elem_key):
                yield elem

    def __container_needs_resizing(self):
        return self.filled_slots + 1 >= (2.0 * self.__get_container_size()) / 3

    def __get_container_size(self):
        return 2 ** self.number_of_low_bits

    def __get_element_container(self):
        return [[None, None, None]] * (2 ** self.number_of_low_bits)

    @classmethod
    def __hash(cls, key):
        return bin(int(hashlib.md5(repr(key)).hexdigest(), 16))

    def __add_element_to_container(self, key, value, container):
        hash_val, index = self.__calculate_index_for_key(key, container)
        container[index] = [hash_val, key, value]

    def __reduce_value_to_number(self, key, perturb):
        hash_val = self.__hash(key)
        last_bits = hash_val[-1 * self.number_of_low_bits:]
        hashed_int = int(last_bits, 2)
        return hash_val, ((5 * hashed_int) + 1 + perturb) % self.__get_container_size()

    def __calculate_index_for_key(self, key, container, perturb=0):
        if key not in calculate_called:
            calculate_called[key] = 0
        calculate_called[key] += 1
        hash_val, index = self.__reduce_value_to_number(key, perturb)
        elem_hash, elem_key, elem_val = container[index]
        if self.__check_elem_non_empty(elem_key) and elem_hash != hash_val:
            return self.__calculate_index_for_key(key, container, perturb + 1)
        return hash_val, index

    def __resize_container(self):
        self.number_of_low_bits += 2
        print 'resizing to ', self.__get_container_size()
        tmp_element_container = self.__get_element_container()
        for elem in self.element_container:
            elem_hash, elem_key, elem_val = elem
            if elem_hash:
                self.__add_element_to_container(elem_key, elem_val, tmp_element_container)
        self.element_container = tmp_element_container

    def __check_elem_non_empty(self, elem_key):
        return elem_key and elem_key != self.deleted_key_dummy_name

    @ExecutionTimer()
    def add(self, key, value):
        if self.__container_needs_resizing():
            self.__resize_container()
        self.__add_element_to_container(key, value, self.element_container)
        self.filled_slots += 1

    def get(self, key):
        hash_val, index = self.__calculate_index_for_key(key, self.element_container)
        if self.element_container[index][0]:
            return self.element_container[index][2]
        return None

    def exists(self, key):
        return self.get(key) is not None

    def remove(self, key):
        hash_val, index = self.__calculate_index_for_key(key, self.element_container)
        if self.element_container[index][0]:
            self.element_container[index] = [None, self.deleted_key_dummy_name, None]

    def __str__(self):
        s = '{'
        for elem in self:
            s += repr(elem[1]) + " : " + repr(elem[2]) + ", "
        return s[:-2] + '}'


a = CustomDict()
calculate_called = {}
for i in range(1350):
    a.add(i, i)
for i in range(1351, 1370):
    a.add(i, i)
sorted(calculate_called.items(), key=lambda x: x[1], reverse=True)
calculate_called = {}
for i in a:
    a.get(i[1])
