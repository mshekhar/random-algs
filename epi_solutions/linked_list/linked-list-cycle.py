# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow_ptr = head
            fast_ptr = head.next

            while slow_ptr != fast_ptr:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            return True
        except:
            pass
        return False
