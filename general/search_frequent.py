def find_min_k(k_freq):
    return min(k_freq, key=k_freq.get)


def search_frequent_items(k, stream):
    k_freq = {}
    min_k = None
    n = 0
    for ele in stream:
        n += 1
        if ele in k_freq:
            k_freq[ele] += 1
            if ele == min_k:
                min_k = find_min_k(k_freq)
        if ele not in k_freq:
            if len(k_freq) < k + 1:
                k_freq[ele] = 1
                min_k = ele
            else:
                k_freq.pop(min_k)
                k_freq[ele] = 1
                min_k = ele

    for ele in k_freq:
        k_freq[ele] = 0

    for ele in stream:
        if ele in k_freq:
            k_freq[ele] += 1
    return [it for it, value in k_freq.items() if value > (n * 1.0 / k)]


from general.data_provider import get_test_case

for test_case in get_test_case('search_frequent_items.tsv'):
    try:
        res = search_frequent_items(test_case['int'], test_case['array(string)'])
        # print test_case['int']
        # print res
        # print test_case['array(string2)']
        # print test_case['array(string)']

        assert set(res) == set(test_case['array(string2)'])
        print test_case
    except AssertionError:
        import time

        time.sleep(0.5)
        raise