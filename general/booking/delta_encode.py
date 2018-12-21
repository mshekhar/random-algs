def delta_encode(array):
    if not array:
        return
    curr = array[0]
    yield curr
    c = 1
    while c < len(array):
        res = array[c] - curr
        if not -127 <= res <= 127:
            yield -128
        yield res
        curr = array[c]
        c += 1


print list(delta_encode([25626, 25757, 24367, 24267, 16, 100, 2, 7277]))
