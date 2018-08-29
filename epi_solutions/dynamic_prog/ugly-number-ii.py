class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        ugly_nums = [1]
        idx_list = [0, 0, 0]
        prime_nums = [2, 3, 5]
        for i in range(1, n):
            while True:
                new_vals = []
                for j in range(len(idx_list)):
                    # print j, idx_list[j], prime_nums[j], ugly_nums[idx_list[j]]
                    new_vals.append(ugly_nums[idx_list[j]] * prime_nums[j])
                ugly_num = min(new_vals)
                min_idx = new_vals.index(ugly_num)
                idx_list[min_idx] += 1
                if ugly_num != ugly_nums[-1]:
                    ugly_nums.append(ugly_num)
                    break
        return ugly_nums[-1]


print Solution().nthUglyNumber(10)
