from heapq import heappush, heappop


class HeapObject(object):
    def __init__(self, num, idx, list_idx):
        self.num = num
        self.idx = idx
        self.list_idx = list_idx

    def __cmp__(self, other):
        return cmp(self.num, other.num)

    def __str__(self):
        return str(self.num) + "___" + str(self.list_idx)


class Solution(object):
    def __init__(self):
        self.min_heap = []
        self.running_min = float('inf')
        self.running_max = float('-inf')
        self.scrolled_indexes = None
        self.range_formed_from = set()

    def initialize_min_heap(self, nums):
        num_lists = len(nums)
        self.scrolled_indexes = [0] * num_lists
        for c, lst in enumerate(nums):
            self.running_min = min(lst[0], self.running_min)
            self.running_max = max(lst[0], self.running_max)
            heappush(self.min_heap, HeapObject(num=lst[0], idx=0, list_idx=c))

    def get_and_set_item_in_heap(self, nums):
        ele = heappop(self.min_heap)
        if ele.idx + 1 < len(nums[ele.list_idx]):
            new_num = nums[ele.list_idx][ele.idx + 1]
            if new_num > self.running_max:
                self.running_max = new_num
            heappush(self.min_heap, HeapObject(num=new_num,
                                               idx=ele.idx + 1,
                                               list_idx=ele.list_idx))
            self.running_min = self.min_heap[0].num
        return ele

    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        self.initialize_min_heap(nums)
        # self.running_min = min(map(lambda x: x.num, self.min_heap))
        # self.running_max = max(map(lambda x: x.num, self.min_heap))
        smallest_range = float('inf')
        range_list = None
        while len(self.min_heap) == len(nums):
            # print map(lambda x: str(x), self.min_heap)

            if self.running_max - self.running_min < smallest_range:
                smallest_range = self.running_max - self.running_min
                range_list = [self.running_min, self.running_max]
            _ = self.get_and_set_item_in_heap(nums)
        return range_list


print Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
print Solution().smallestRange([[1]])
