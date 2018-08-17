# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def print_ll(cls, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            if curr.next:
                curr = curr.next
            else:
                break
        return arr


class Solution(object):
    def get_list_len(self, head):
        list_len = 1
        curr = head
        while curr:
            if curr.next:
                curr = curr.next
                list_len += 1
            else:
                break
        return list_len

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        list_len = self.get_list_len(head)
        rotate_len = k % list_len
        start_ptr = head
        end_ptr = head
        for i in range(rotate_len):
            nxt_obj = end_ptr.next
            if nxt_obj:
                end_ptr = nxt_obj
        # print end_ptr.val, start_ptr.val

        while True:
            if end_ptr.next:
                start_ptr = start_ptr.next
                end_ptr = end_ptr.next
            else:
                break
        # print end_ptr.val, start_ptr.val

        end_ptr.next = head
        new_head = start_ptr.next
        start_ptr.next = None

        return new_head

    @classmethod
    def construct_ll(cls, arr):
        head = None
        curr = None
        for i in arr:
            n = ListNode(i)
            if head is None:
                head = n
                curr = n
            else:
                curr.next = n
                curr = n
        return head


print ListNode.print_ll(Solution().rotateRight(Solution.construct_ll([1, 2, 3, 4, 5]), 2))
print ListNode.print_ll(Solution().rotateRight(Solution.construct_ll([0, 1, 2]), 4))
