def maximum_tip(n, x, y, arr_x, arr_y):
    tmp_arr = []
    for i in range(n):
        tmp_arr.append((arr_x[i], arr_y[i]))
    tmp_arr.sort(key=lambda tmp: abs(tmp[0] - tmp[1]), reverse=True)

    max_tip = 0

    for tip_x, tip_y in tmp_arr:
        if x <= 0:
            max_tip += tip_y
            continue
        elif y <= 0:
            max_tip += tip_x
            continue
        else:
            if tip_x >= tip_y:
                x -= 1
                max_tip += tip_x
            else:
                y -= 1
                max_tip += tip_y
    return max_tip


# print maximum_tip(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

raw_input = input  # for python 31


def abc():
    t = int(raw_input())
    for _ in range(t):
        n, x, y = list(map(lambda x: int(x), filter(None, raw_input().split(" "))))
        print(maximum_tip(n, x, y,
                          list(map(lambda x: int(x), filter(None, raw_input().split(" ")))),
                          list(map(lambda x: int(x), filter(None, raw_input().split(" "))))))


abc()
# 2
# 5 3 3
# 1 2 3 4 5
# 5 4 3 2 1
# 8 4 4
# 1 4 3 2 7 5 9 6
# 1 2 3 6 5 4 9 8
# 7 3 4
# 8 7 5 9 6 6 8
# 1 7 5 1 2 3 9
