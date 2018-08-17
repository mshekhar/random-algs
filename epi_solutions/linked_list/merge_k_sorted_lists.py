# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __cmp__(self, other):
        return cmp(self.val, other.val)

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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # print lists
        # print map(lambda x: ListNode.print_ll(x), lists)

        min_heap = []
        head = None
        curr = None
        for i in lists:
            if i:
                heapq.heappush(min_heap, (i.val, i))
        # print 'min heap', map(lambda x: x[0], min_heap)
        while min_heap:
            ele = heapq.heappop(min_heap)
            if head is None:
                # print 'first ele', ele[0]
                head = ele[1]
                curr = ele[1]
            else:
                # print 'ele', ele[0]
                curr.next = ele[1]
                curr = curr.next
            if ele[1].next:
                heapq.heappush(min_heap, (ele[1].next.val, ele[1].next))
        # print ListNode.print_ll(head)
        return head

    @classmethod
    def construct_lls(cls, arrs):
        res = []
        for arr in arrs:
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
            res.append(head)
        return res


# print map(lambda x: ListNode.print_ll(x), Solution().construct_lls([
#     [1, 4, 5],
#     [1, 3, 4],
#     [2, 6]
# ]))

print ListNode.print_ll(Solution().mergeKLists(Solution.construct_lls([[1, 4, 5], [1, 3, 4], [2, 6]])))

# print ListNode.print_ll(Solution().mergeKLists(Solution.construct_lls([[]])))
