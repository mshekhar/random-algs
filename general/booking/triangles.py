#!/bin/python


# Complete the triangle function below.
def triangle(a, b, c):
    triangle_possible = a + b > c and a + c > b and b + c > a
    if not triangle_possible:
        return 0
    else:
        if a == b == c:
            return 1
        return 2


if __name__ == '__main__':
    pass
