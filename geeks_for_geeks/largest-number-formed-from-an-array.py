import functools


def compare(num1, num2):
    return int(num1 + num2) - int(num2 + num1)


def largest_number(arr):
    return "".join(sorted(arr, key=functools.cmp_to_key(compare), reverse=True))


def abc():
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        print(largest_number(list(filter(None, raw_input().split(" ")))))


raw_input = input  # for python 31
abc()
# 2
# 5
# 3 30 34 5 9
# 4
# 54 546 548 60
