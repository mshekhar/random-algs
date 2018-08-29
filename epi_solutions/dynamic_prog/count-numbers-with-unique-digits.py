class Solution(object):
    # sol_map = {0: 1, 1: 10, 2: 91, 3: 739, 4: 5275, 5: 32491, 6: 168571, 7: 712891, 8: 2345851, 9: 5611771, 10: 8877691,
    #            11: 8877691, 12: 8877691, 13: 8877691, 14: 8877691, 15: 8877691, 16: 8877691, 17: 8877691, 18: 8877691,
    #            19: 8877691, 20: 8877691}
    sol_lst = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691, 8877691, 8877691, 8877691,
               8877691, 8877691, 8877691, 8877691, 8877691, 8877691, 8877691]
    sol_lst_len = len(sol_lst)

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= self.sol_lst_len:
            return 8877691
        return self.sol_lst[n]
        if not n:
            return 1
        # single digit sum
        sol = 10
        st = 9
        st_arr = [9]
        for i in range(1, n):
            if 10 - i <= 0:
                break
            st_arr.append(10 - i)
            # print i, n, st_arr
            st *= (10 - i)
            sol += st
        return sol


# temp_arr = [0] * len(Solution.sol_map)
# for i in Solution.sol_map:
#     temp_arr[i] = Solution.sol_map[i]
# print temp_arr
for i in range(0, 21):
    print Solution().countNumbersWithUniqueDigits(i)
