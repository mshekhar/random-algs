class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        num_zeros_one = [0, 0]
        str_as_num_arr = map(lambda x: int(x), A)

        best_start = best_end = start = end = -1
        res_config = [0, 0]

        start = end = 0
        for c, i in enumerate(str_as_num_arr):
            num_zeros_one[i] += 1
            # print 'before ', num_zeros_one, res_config
            if (num_zeros_one[0] - num_zeros_one[1]) > (res_config[0] - res_config[1]):
                best_start = start
                best_end = end
                res_config = num_zeros_one[:]
            end += 1

            if num_zeros_one[1] > num_zeros_one[0]:
                num_zeros_one = [0, 0]
                start = end = c + 1
                if i == 0:
                    start = end = c
                    num_zeros_one[0] += 1
            # print c, i, start, end, best_start, best_end, res_config, num_zeros_one
        if best_start == best_end == -1:
            return []
        return [best_start + 1, best_end + 1]


print Solution().flip('0010')
print Solution().flip('111')
print Solution().flip('011')
print Solution().flip('')
