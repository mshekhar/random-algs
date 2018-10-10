# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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


class Solution(object):
    def reverseList(self, head, head_prev):
        curr = head
        prev_pointer = None
        while curr:
            tmp = curr.next
            curr.next = prev_pointer
            # print 'pointing ', curr.val, 'to', None if prev_pointer is None else prev_pointer.val, tmp
            prev_pointer = curr
            curr = tmp
        head_prev.next = None
        return prev_pointer

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        # middle of linked list
        if not head:
            return
            # return head
        p1 = head
        p2 = head
        while p1.next and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        # print p1.val, p2.val
        if not p1.next:
            return
        tail = self.reverseList(p1.next, p1)
        # print ListNode.print_ll(head), ListNode.print_ll(tail)

        curr_1 = head
        curr_2 = tail

        while curr_1 and curr_2:
            tmp1 = curr_1.next
            tmp2 = curr_2.next

            curr_2.next = tmp1
            curr_1.next = curr_2

            curr_1 = tmp1
            curr_2 = tmp2

        # return head

    @classmethod
    def driver(cls, arr):
        head = ListNode.construct_ll(arr)
        Solution().reorderList(head)
        return ListNode.print_ll(head)


print Solution().driver([1, 2, 3, 4])
print Solution().driver([1, 2, 3, 4, 5])
print Solution().driver([1])
print Solution().driver([])
