# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detect_loop(self, head):
        try:
            slow_ptr = head
            fast_ptr = head.next

            while slow_ptr != fast_ptr:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            return slow_ptr
        except:
            pass
        return None

    def detect_cycle(self, ptr_1, ptr_2):
        while ptr_1 != ptr_2:
            # print 'ptr_1', ptr_1.val, 'ptr_2', ptr_2.val
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
        return ptr_1

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation
        loop_node = self.detect_loop(head)
        if loop_node:
            # print loop_node.val, head.val
            return self.detect_cycle(head, loop_node.next)
        return None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next

print Solution().detectCycle(head).val
print Solution().detectCycle(None)
