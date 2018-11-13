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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        slow_ptr = head
        fast_ptr = head
        i = 1
        while i <= n:
            fast_ptr = fast_ptr.next
            i += 1

        while fast_ptr:
            fast_ptr = fast_ptr.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        prev.next = slow_ptr.next
        return dummy.next


print Solution.print_ll(Solution().removeNthFromEnd(Solution.construct_ll([1, 2, 3, 4, 5]), 1))
print Solution.print_ll(Solution().removeNthFromEnd(Solution.construct_ll([1, 2, 3, 4, 5]), 2))
print Solution.print_ll(Solution().removeNthFromEnd(Solution.construct_ll([1, 2, 3, 4, 5]), 3))
print Solution.print_ll(Solution().removeNthFromEnd(Solution.construct_ll([1, 2, 3, 4, 5]), 4))
print Solution.print_ll(Solution().removeNthFromEnd(Solution.construct_ll([1, 2, 3, 4, 5]), 5))
