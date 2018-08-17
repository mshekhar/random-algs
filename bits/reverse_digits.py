import random
import sys


def reverse_number(number):
    r_number = 0
    abs_number = abs(number)
    while abs_number > 0:
        r_number = r_number * 10 + abs_number % 10
        abs_number /= 10
    return -r_number if number < 0 else r_number


def check_ans(x):
    s = str(x)
    s = '-' + s[:0:-1] if s[0] == '-' else s[::-1]
    return int(s)


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print('n = %d, reversed n = %d' % (n, reverse_number(n)))
        assert check_ans(n) == reverse_number(n)
    else:
        for _ in range(1000):
            n = random.randint(-sys.maxsize, sys.maxsize)
            print('n = %d, reversed n = %d' % (n, reverse_number(n)))
            assert check_ans(n) == reverse_number(n)


if __name__ == '__main__':
    main()
