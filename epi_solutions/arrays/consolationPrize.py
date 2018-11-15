#!/usr/bin/env python


def counting_sort(array, maxval):
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m  # init with zeros
    for a in array:
        count[a] += 1  # count occurences
    i = 0
    for a in range(m):  # emit
        for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array[::-1]


def take_input():
    s = raw_input()
    n = int(s.split()[0])
    k = int(s.split()[1])
    s = raw_input()
    array = list()
    for i in s.split():
        array.append(int(i))

    array = counting_sort(array, 100)

    print len(array[k - 1:])


take_input()
