class Solution(object):
    def get_mtx_val(self, row, col, mtx):
        if row < 0 or col < 0:
            raise IndexError()
        return mtx[row][col]

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        try:
            m = len(matrix)
            n = len(matrix[0])
            if m < 1 or n < 1:
                return []
        except IndexError:
            return []
        indices_set = [[0, 1, 1, 0, n, 1],
                       [1, m, 1, n - 1, n, 1],
                       [m - 1, m, 1, n - 2, -1, -1],
                       [m - 2, 0, -1, 0, 1, 1]]
        operator = [[1, 1, 0, 1, -1, 0],
                    [1, -1, 0, -1, -1, 0],
                    [-1, -1, 0, -1, 1, 0],
                    [-1, 1, 0, 1, 1, 0]]
        res = []
        tracker_i = set()
        tracker_j = set()
        end_condition = [0, 0, 0, 0]
        while True:
            for c, indices in enumerate(indices_set):
                if sum(end_condition) >= 4:
                    return res
                start_i, end_i, direction_i = indices[0:3]
                start_j, end_j, direction_j = indices[3:]
                if direction_i == 1 and start_i > end_i:
                    end_condition[0] = 1
                    continue
                if direction_i == -1 and start_i < end_i:
                    end_condition[1] = 1
                    continue
                if direction_j == 1 and start_j > end_j:
                    end_condition[2] = 1
                    continue
                if direction_j == -1 and start_j < end_j:
                    end_condition[3] = 1
                    continue

                if c == 0 or c == 2:
                    if (start_i, end_i) in tracker_i:
                        continue
                    tracker_i.add((start_i, end_i))

                elif c == 1 or c == 3:
                    if (start_j, end_j) in tracker_j:
                        continue
                    tracker_j.add((start_j, end_j))

                for i in range(start_i, end_i, -1 if direction_i == -1 else 1):
                    for j in range(start_j, end_j, -1 if direction_j == -1 else 1):
                        # print i, j, matrix[i][j]
                        try:
                            res.append(self.get_mtx_val(i, j, matrix))
                        except IndexError:
                            pass

            new_indices_set = []
            for c, idx in enumerate(indices_set):
                new_indices_set.append([x + y for x, y in zip(operator[c], idx)])

            # print indices_set
            # print new_indices_set
            indices_set = new_indices_set

        return res


print Solution().spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

print Solution().spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]), [1, 2, 3, 6, 9, 8, 7, 4, 5]

print Solution().spiralOrder([
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]), [1, 5, 9, 10, 11, 12, 8, 4, 3, 2, 6, 7]

print Solution().spiralOrder([
    []
]), []
print Solution().spiralOrder([
    [1]
]), [1]

print Solution().spiralOrder([
    [6, 9, 7]
]), [6, 9, 7]

print Solution().spiralOrder([
    [6], [9], [7]
]), [6, 9, 7]
