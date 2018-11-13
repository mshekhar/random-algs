# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
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

    def get_ll_len(self, head):
        ll_len = 0
        curr = head
        while curr:
            ll_len += 1
            curr = curr.next
        return ll_len

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ll_len = self.get_ll_len(head)
        dummy = ListNode(0)
        dummy.next = head
        pair_size = 1
        # import pdb
        # pdb.set_trace()
        while pair_size < ll_len:
            print 'starting pair ', pair_size, self.print_ll(dummy.next)
            prev = dummy
            curr = dummy.next
            while curr:
                left_start, left_end = curr, self.split(curr, pair_size)
                # print 'left_start, left_end', left_start.val if left_start else None, left_end.val if left_end else None
                if not left_end:
                    right_start, right_end = None, None
                else:
                    right_start, right_end = left_end.next, self.split(left_end.next, pair_size)
                # print 'right_start, right_end', right_start.val if right_start else None, right_end.val if right_end else None
                prev = self.merge(left_start, left_end, right_start, right_end, pair_size, prev)
                # print 'prev', prev.val if prev else None
                curr = prev.next
            pair_size <<= 1
        return dummy.next

    def split(self, head, pair_size):
        if not head:
            return None
        curr = head
        count = 1
        while curr and count < pair_size:
            curr = curr.next
            count += 1

        return curr

    def merge(self, left_start, left_end, right_start, right_end, pair_size, prev):
        curr = prev
        left_curr = left_start
        right_curr = right_start
        left_count = 0
        right_count = 0

        while left_curr and right_curr and left_count < pair_size and right_count < pair_size:
            if left_curr.val < right_curr.val:
                curr.next = left_curr
                left_curr = left_curr.next
                left_count += 1
            else:
                curr.next = right_curr
                right_curr = right_curr.next
                right_count += 1
            curr = curr.next

        if left_curr and left_count < pair_size:
            if left_end:
                left_end.next = right_end.next if right_end else None
            while left_curr and left_count < pair_size:
                curr.next = left_curr
                left_curr = left_curr.next
                left_count += 1
                curr = curr.next
        elif right_curr and right_count < pair_size:
            while right_curr and right_count < pair_size:
                curr.next = right_curr
                right_curr = right_curr.next
                right_count += 1
                curr = curr.next
        return curr


print Solution.print_ll(Solution().sortList(Solution.construct_ll([-1, 5, 3, 4, 0])))
print Solution.print_ll(Solution().sortList(Solution.construct_ll([4, 2, 1, 3])))
