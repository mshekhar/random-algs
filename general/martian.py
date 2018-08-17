# MARTIAN
# http://www.spoj.com/problems/MARTIAN/

bloggium = []
yeyenum = []
agg_bloggium = []
agg_yeyenum = []
max_minerals = []


def get_input():
    n, m = map(lambda x: int(x), raw_input().split(' '))
    for i in range(n):
        yeyenum.append(map(lambda x: int(x), raw_input().split(' ')))
    for i in range(n):
        bloggium.append(map(lambda x: int(x), raw_input().split(' ')))
    n_zero, m_zero = map(lambda x: int(x), raw_input().split(' '))
    init_max_minerals(n, m)
    return n, m


def init_max_minerals(n, m):
    for i in range(n):
        max_minerals.append(map(lambda _: 0, range(m)))
        agg_yeyenum.append(map(lambda _: 0, range(m)))
        agg_bloggium.append(map(lambda _: 0, range(m)))


def is_valid_index(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    return False


def get_value_at_index(i, j, n, m, arr):
    return arr[i][j] if is_valid_index(i, j, n, m) else 0


def get_max_mineral_count(n, m):
    for i in range(n):
        for j in range(m):
            agg_bloggium[i][j] = get_value_at_index(i - 1, j, n, m, agg_bloggium) + bloggium[i][j]
            agg_yeyenum[i][j] = get_value_at_index(i, j - 1, n, n, agg_yeyenum) + yeyenum[i][j]

            max_minerals[i][j] = max(get_value_at_index(i - 1, j, n, m, max_minerals) + agg_yeyenum[i][j],
                                     get_value_at_index(i, j - 1, n, m, max_minerals) + agg_bloggium[i][j])


def driver():
    n, m = get_input()
    # print bloggium
    # print yeyenum
    # print n, m
    # print agg_bloggium
    # print agg_yeyenum
    # print max_minerals
    get_max_mineral_count(n, m)
    return max_minerals[n - 1][m - 1]


print driver()

# n, m = 4, 4
# yeyenum = [
#     [0, 0, 10, 9],
#     [1, 3, 10, 0],
#     [4, 2, 1, 3],
#     [1, 1, 20, 0]
# ]
# bloggium = [
#     [10, 0, 0, 0],
#     [1, 1, 1, 30],
#     [0, 0, 5, 5],
#     [5, 10, 10, 10]
# ]
# init_max_minerals(n, m)
# get_max_mineral_count(n, m)
# print max_minerals[n-1][m-1]
