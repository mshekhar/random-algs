def a():
    for i in range(10):
        yield i

print a().next()