# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @classmethod
    def convert_list_to_ll(cls, lst):
        curr = None
        head = None
        for i in lst:
            n = ListNode(i)
            if curr is None:
                curr = n
                head = n
            else:
                curr.next = n
                curr = n
        return head

    @classmethod
    def convert_ll_to_list(cls, head):
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

    def reverse_list(self, head, head_prev, k):
        counter = 1
        curr_head = head
        curr = head
        while counter < k:
            tmp = curr.next
            next_ele = None
            if tmp:
                next_ele = curr.next.next
            tmp.next = curr_head
            curr.next = next_ele
            curr_head = tmp
            counter += 1
        if head_prev:
            head_prev.next = curr_head
        return curr_head, curr

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_prev = None
        curr = head
        batch_head = head
        counter = 1
        while curr and curr.next:
            curr = curr.next
            counter += 1
            if counter == k:
                # print 'calling reverse', batch_head.val, curr.val, head_prev
                # import pdb
                # pdb.set_trace()
                tmp_head, tmp_tail = self.reverse_list(batch_head, head_prev, k)
                # print 'reversed', tmp_head.val, tmp_tail.val
                if head_prev is None:
                    head = tmp_head
                head_prev = tmp_tail
                counter = 1
                curr = tmp_tail.next
                batch_head = curr
        return head


arr = [1, 2, 3, 4, 1, 2, 6, 7, 8]
print arr
# print Solution.convert_ll_to_list(Solution().reverse_list(Solution.convert_list_to_ll(arr), None, len(arr))[0])
print Solution.convert_ll_to_list(Solution().reverseKGroup(Solution.convert_list_to_ll(arr), 3))
print Solution.convert_ll_to_list(Solution().reverseKGroup(Solution.convert_list_to_ll(arr), 2))
print Solution.convert_ll_to_list(Solution().reverseKGroup(Solution.convert_list_to_ll(arr), 0))
