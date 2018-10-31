import Queue
import collections


class Solution(object):
    def can_get_hands_from_chunk(self, chunk, W):
        chunk_min = min(chunk.keys())
        # print chunk, chunk_min
        while chunk and len(chunk) >= W:
            i = 0
            tmp_min = chunk_min
            while i != W and chunk:
                chunk[tmp_min] -= 1
                if chunk[tmp_min] <= 0:
                    chunk.pop(tmp_min)
                    chunk_min += 1
                tmp_min += 1
                i += 1
            # print chunk, chunk_min, tmp_min
            if i < W:
                return False
        if chunk:
            return False
        return True

    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if W < 1:
            return False
        counter = collections.Counter()
        for i in hand:
            counter[i] += 1

        # print counter
        while counter:
            q = Queue.Queue()
            q.put(counter.popitem())
            chunk = collections.Counter()
            while not q.empty():
                num, count = q.get()
                chunk[num] = count
                next_ele = num + 1
                prev_ele = num - 1

                if next_ele in counter:
                    q.put((next_ele, counter.pop(next_ele)))
                if prev_ele in counter:
                    q.put((prev_ele, counter.pop(prev_ele)))
            if not self.can_get_hands_from_chunk(chunk, W):
                return False

        return True


# print Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
# print Solution().isNStraightHand([1, 2, 3, 4, 5], 3)
# print Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 7, 8], 3)
# print Solution().isNStraightHand([1, 2], 3)
# print Solution().isNStraightHand([], 3)
# print Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 1)
# print Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 0)
# print Solution().isNStraightHand([1, 1, 2, 2, 3, 3], 2)
print Solution().isNStraightHand([8, 6, 5, 7, 9], 5)
