from utils.linked_lists.single_linked_list import LinkedList


class MergeSort(object):
    @staticmethod
    def insert_node(linked_list, node_to_insert, next_node, insert_location):
        insert_location.next_obj = node_to_insert
        node_to_insert.next_obj = next_node
        linked_list.insert_node(node_to_insert, insert_location)
        return node_to_insert

    @staticmethod
    def merge_sorted_linked_lists(linked_list_a, linked_list_b):
        linked_list_c = LinkedList()
        linked_list_a_gen = linked_list_a.pop()
        linked_list_b_gen = linked_list_b.pop()
        try:
            node_a = next(linked_list_a_gen)
        except StopIteration:
            linked_list_a = linked_list_b
            return linked_list_a
        try:
            node_b = next(linked_list_b_gen)
        except StopIteration:
            return linked_list_a
        while True:
            if node_a.data > node_b.data:
                linked_list_c.insert_node(node_b)
                node_b = next(linked_list_b_gen, None)
                if node_b is None:
                    linked_list_c.insert_node(node_a)
                    break
            else:
                linked_list_c.insert_node(node_a)
                node_a = next(linked_list_a_gen, None)
                if node_a is None:
                    linked_list_c.insert_node(node_b)
                    break
        while True:
            node_b = next(linked_list_b_gen, None)
            if node_b is None:
                break
            linked_list_c.insert_node(node_b)
        while True:
            node_a = next(linked_list_a_gen, None)
            if node_a is None:
                break
            linked_list_c.insert_node(node_a)
        return linked_list_c

    @staticmethod
    def divide_list(linked_list, factor=2):
        count = 0
        linked_list_a = LinkedList()
        linked_list_a.head = linked_list.head
        linked_list_b = LinkedList()
        linked_list_b.tail = linked_list.tail
        for node in linked_list.traverse():
            count += 1
            if count >= linked_list.length / factor:
                next_node = node.next_obj
                node.next_obj = None
                linked_list_a.tail = node
                linked_list_a.length = count
                linked_list_b.length = linked_list.length - count
                linked_list_b.head = next_node
                return linked_list_a, linked_list_b

    @staticmethod
    def sort(linked_list):
        if linked_list.length <= 1:
            return linked_list
        linked_list_a, linked_list_b = MergeSort.divide_list(linked_list)
        linked_list_a = MergeSort.sort(linked_list_a)
        linked_list_b = MergeSort.sort(linked_list_b)
        return MergeSort.merge_sorted_linked_lists(linked_list_a, linked_list_b)
