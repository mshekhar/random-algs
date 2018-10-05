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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res_head = None
        res_curr = None
        cur_1 = l1
        cur_2 = l2
        carry = 0

        while cur_1 or cur_2:
            res = carry
            if cur_1:
                # print 'cur_1 val ', cur_1.val
                res += cur_1.val
                cur_1 = cur_1.next
            if cur_2:
                # print 'cur_2 val ', cur_2.val
                res += cur_2.val
                cur_2 = cur_2.next
            carry = 1 if res >= 10 else 0
            new_val = res % 10 if res >= 10 else res
            # print 'new node ', res, carry
            t = ListNode(new_val)
            if not res_head:
                res_head = t
                res_curr = t
            else:
                res_curr.next = t
                res_curr = t

        if carry:
            t = ListNode(carry)
            res_curr.next = t
            res_curr = t

        # while res_head and res_head.val == 0:
        #     res_head = res_head.next

        return res_head


print ListNode.print_ll(Solution().addTwoNumbers(ListNode.construct_ll([2, 4, 3]), ListNode.construct_ll([5, 6, 4])))
print ListNode.print_ll(Solution().addTwoNumbers(ListNode.construct_ll([2, 4, 3]), ListNode.construct_ll([0])))
print ListNode.print_ll(Solution().addTwoNumbers(ListNode.construct_ll([4]), ListNode.construct_ll([6])))
print ListNode.print_ll(Solution().addTwoNumbers(ListNode.construct_ll([0]), ListNode.construct_ll([1, 8])))
print ListNode.print_ll(
    Solution().addTwoNumbers(ListNode.construct_ll([1, 2, 3, 4, 5, 6]), ListNode.construct_ll([7, 8])))
