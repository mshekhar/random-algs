import heapq


def minimum_plaforms(num_of_trains, train_times):
    train_times.sort(key=lambda x: x[0])
    min_heap = []
    peak_concurrent = 0
    for call in train_times:
        begin = call[0]
        end = call[1]
        while min_heap and begin > min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)
        peak_concurrent = max(peak_concurrent, len(min_heap))
    return peak_concurrent


raw_input = input # for python 3

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    train_times = zip(map(lambda x: int(x), filter(None, raw_input().split(" "))),
                      map(lambda x: int(x), filter(None, raw_input().split(" "))))
    print minimum_plaforms(len(train_times), train_times)

# 1
# 6
# 900  940 950  1100 1500 1800
# 910 1200 1120 1130 1900 2000

# 79
# 6 552 244 936 151 1604 1110 301 1448 529 1125 930 236 1651 640 1712 1042 305 1032 222 756 1722 1954 503 1515 1422 1632 727 1626 1635 137 341 601 1 1439 401 1756 126 1126 1613 9 1717 820 19 149 928 1525 1031 704 102 1 1237 333 430 1242 546 1433 305 1505 553 553 1129 1638 1528 534 1800 1950 538 1705 732 821 256 838 1717 247 35 132 1730 1522
# 1448 1200 700 1600 1818 1608 1128 1523 1539 543 1141 1158 244 2037 1958 1734 1054 838 1040 900 1928 1755 2027 2026 1552 1609 1633 800 1639 1652 1100 2309 614 1611 1518 1331 2235 1705 1130 1620 200 2000 855 600 854 930 1639 1053 2158 1317 1727 2053 900 528 1254 555 1454 2300 1509 1700 1800 1834 1709 1557 1924 1831 1956 557 1705 951 2300 2138 1334 1746 1900 245 1700 2101 2359

