# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        curr = head
        while curr:
            new_node = RandomListNode(curr.label)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # print head, head.next
        # import pdb
        # pdb.set_trace()
        new_head = head.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        return new_head


print Solution().copyRandomList(RandomListNode(1))
