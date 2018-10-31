class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        index_map = [float('-inf') for _ in range(10)]
        temp_num = num
        num_as_array = []
        while temp_num:
            digit = temp_num % 10
            temp_num /= 10
            num_as_array.append(digit)
        num_as_array = num_as_array[::-1]

        for i in range(len(num_as_array) - 1, -1, -1):
            index_map[num_as_array[i]] = max(index_map[num_as_array[i]], i)

        # print num
        # print num_as_array
        # print index_map

        for c, i in enumerate(num_as_array):
            for num in range(9, -1, -1):
                if num > i and index_map[num] > c:
                    num_as_array[c] = num
                    num_as_array[index_map[num]] = i
                    # print num_as_array
                    return int(''.join(map(str, num_as_array)))
        return int(''.join(map(str, num_as_array)))


print Solution().maximumSwap(72736)
print Solution().maximumSwap(9973)
print Solution().maximumSwap(19973)
