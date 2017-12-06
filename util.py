#! /usr/bin/env python3


from itertools import permutations
from collections import defaultdict, namedtuple, Counter


# 2-D points using (x, y) tuples
def X(point): return point[0]
def Y(point): return point[1]


def neighbours4(point):
    'Without diagonals'
    x, y = point
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def neighbours8(point):
    'With diagonals'
    x, y = point
    return [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
            (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]


def manhattan_distance(p, q):
    return (abs(X(p) - X(q)) + abs(Y(p) - Y(q)))


cat = ''.join


def trace(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('func: {}\targs: {}\tkwargs: {}\tret: {}'
              .format(func.__name__, args, kwargs, ret))
        return ret
    return inner


if __name__ == '__main__':

    @trace
    def sum(a, b):
        return a + b

    sum(1, 2)
