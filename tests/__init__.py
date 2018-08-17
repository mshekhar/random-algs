# def get_idx_value(k, m, mtx):
#     try:
#         if k >= 0 and m >= 0:
#             return mtx[k][m]
#     except IndexError:
#         return None
#     return None
#
#
# def get_finished_idx_value(k, m, finished_mtx):
#     try:
#         if k >= 0 and m >= 0:
#             return finished_mtx[k][m]
#     except IndexError:
#         pass
#     return None
#
#
# def count_connections(matrix):
#     # matrix = [[1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 0, 1]]
#     finished_mtx = map(lambda x: map(lambda y: 0, x), matrix)
#     count_conn = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j]:
#                 for k, m in [(i + 1, j), (i - 1, j), (i - 1, j - 1), (i, j - 1),
#                              (i + 1, j - 1), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
#                     # if k == -1 and m == 0:
#                     #     import pdb
#                     #     pdb.set_trace()
#                     v1 = get_idx_value(k, m, matrix)
#                     if v1:
#                         v2 = get_finished_idx_value(k, m, finished_mtx)
#                         if not v2:
#                             # print k, m, i, j, v1, matrix[i][j]
#                             count_conn += 1
#             finished_mtx[i][j] = 1
#     return count_conn

# for (int i = 0; i < matrix.size(); i++) {
#             int min = 0;
#             int max = 0;
#             for (int j = 0; j < matrix.get(i).size(); j++) {
#                 int val = matrix.get(i).get(j);
#                 if (val < matrix.get(i).get(min)) min = j;
#                 if (val > matrix.get(i).get(max)) max = j;
#             }
#             markedMin[i][min] = true;
#             markedMax[i][max] = true;
#         }
class DummyException(Exception):
    pass


def get_idx_value(k, m, matrix):
    try:
        if k >= 0 and m >= 0:
            return matrix[k][m]
    except IndexError:
        pass
    return None


def get_row_wise_min_max(matrix):
    marked_min = map(lambda x: map(lambda y: False, x), matrix)
    marked_max = map(lambda x: map(lambda y: False, x), matrix)

    for i in range(len(matrix)):
        min_val = 0
        max_val = 0
        for j in range(len(matrix[i])):
            v1 = get_idx_value(i, j, matrix)
            if v1:
                v_min = get_idx_value(i, min_val, matrix)
                v_max = get_idx_value(i, max_val, matrix)
                if v1 < v_min:
                    min_val = j
                if v1 > v_max:
                    max_val = j

        marked_min[i][min_val] = True
        marked_max[i][max_val] = True

    print marked_max
    print marked_min
    for i in range(len(marked_min)):
        c = 0
        for j in range(len(marked_min[i])):
            if get_idx_value(i, j, marked_min):
                c += 1
        if c > 1:
            raise DummyException()

    for i in range(len(marked_max)):
        c = 0
        for j in range(len(marked_max[i])):
            if get_idx_value(i, j, marked_max):
                c += 1
        if c > 1:
            raise DummyException()

    return marked_min, marked_max


def get_column_wise_min_max(matrix):
    marked_min = map(lambda x: map(lambda y: False, x), matrix)
    marked_max = map(lambda x: map(lambda y: False, x), matrix)

    for j in range(len(matrix[0])):
        min_val = 0
        max_val = 0
        for i in range(len(matrix)):
            v1 = get_idx_value(i, j, matrix)
            v_min = get_idx_value(min_val, j, matrix)
            v_max = get_idx_value(max_val, j, matrix)
            if v1 < v_min:
                min_val = i
            if v1 > v_max:
                max_val = i
        print 'column wise', min_val, max_val, j
        marked_min[min_val][j] = True
        marked_max[max_val][j] = True

    print marked_max
    print marked_min
    for i in range(len(marked_min)):
        c = 0
        for j in range(len(marked_min[i])):
            if get_idx_value(i, j, marked_min):
                c += 1
        if c > 1:
            raise DummyException()

    for i in range(len(marked_max)):
        c = 0
        for j in range(len(marked_max[i])):
            if get_idx_value(i, j, marked_max):
                c += 1
        if c > 1:
            raise DummyException()

    return marked_min, marked_max


def getSpecialElements(matrix):
    try:
        marked_min_1, marked_max_1 = get_row_wise_min_max(matrix)
        marked_min_2, marked_max_2 = get_column_wise_min_max(matrix)

        marked_min = marked_min_1
        for i in range(len(marked_min_2)):
            for j in range(len(marked_min_2[i])):
                marked_min[i][j] = marked_min[i][j] or marked_min_2[i][j]

        marked_max = marked_max_1
        for i in range(len(marked_max_2)):
            for j in range(len(marked_max_2[i])):
                marked_max[i][j] = marked_max[i][j] or marked_max_2[i][j]

        print marked_min
        print marked_max

        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if get_idx_value(i, j, marked_min) or get_idx_value(i, j, marked_max):
                    result += 1

        return result
    except DummyException:
        import time
        time.sleep(0.4)
        raise
        return -1


# print getSpecialElements([[1, 3, 4], [5, 2, 9], [8, 7, 6]])
# print get_row_wise_min_max([[1, 2, 4], [5, 3, 9], [8, 7, 6]])
print '\n\n\n'
# print get_column_wise_min_max([[1, 2, 4], [5, 3, 9], [8, 7, 6]])

# print getSpecialElements([[1, 2, 4], [5, 3, 9], [8, 7, 6]])
print getSpecialElements([[1, 3, 4], [5, 2, 9], [8, 7, 6]])
