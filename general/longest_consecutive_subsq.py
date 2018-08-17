import Queue


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = set()
        for i in nums:
            nums_map.add(i)

        longest_seq = 0
        while nums_map:
            seq_count = 1
            q = Queue.Queue(maxsize=len(nums))
            q.put(nums_map.pop())
            while not q.empty():
                ele = q.get()
                next_ele = ele + 1
                prev_ele = ele - 1

                if next_ele in nums_map:
                    seq_count += 1
                    q.put(next_ele)
                    nums_map.remove(next_ele)
                if prev_ele in nums_map:
                    seq_count += 1
                    q.put(prev_ele)
                    nums_map.remove(prev_ele)
            if seq_count > longest_seq:
                longest_seq = seq_count
        return longest_seq


# print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
# print Solution().longestConsecutive([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42])
