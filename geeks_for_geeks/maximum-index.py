# https://practice.geeksforgeeks.org/problems/maximum-index/0

def maximum_index(arr):
    min_left = []
    running_min = float('inf')
    running_min_idx = float('inf')
    for c, i in enumerate(arr):
        if i < running_min:
            running_min = i
            running_min_idx = c
        min_left.append(running_min_idx)

    max_right = []
    running_max = float('-inf')
    running_max_idx = float('-inf')
    c = len(arr) - 1
    while c >= 0:
        i = arr[c]
        if i > running_max:
            running_max = i
            running_max_idx = c
        max_right.append(running_max_idx)
        c -= 1

    print max_right
    print min_left


# raw_input = input  # for python 31


def abc():
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        print(maximum_index(map(lambda x: int(x), filter(None, raw_input().split(" ")))))


# abc()


def be(n):
    b = 0
    while n > 0:
        b += n & 1
        n /= 2
    return b


for i in range(1, 10):
    print 2 ** (i - 1), (2 ** i) - 1, sum(map(lambda x: be(x), range(2 ** (i - 1), (2 ** i))))

import math
math.log(10**18)