#! /usr/bin/env python3


from itertools import permutations
from functools import partial
from collections import defaultdict, namedtuple, Counter


cat = ''.join
letters = 'abcdefghipqrstuvwxyz'


inc = partial(sum, 1)
dec = partial(sum, -1)


def zipwith(func, seq1, seq2):
    'Join two lists by applying a function to corresponding elements'
    return [func(*t) for t in zip(seq1, seq2)]


def chunks(seq, size):
    chunks = []
    while len(seq) > 0:
        chunks.append(seq[:size])
        seq = seq[size:]
    return chunks


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


def is_in_bounds(size, point):
    return 0 <= X(point) < size and 0 <= Y(point) < size


def manhattan_distance(p, q):
    return (abs(X(p) - X(q)) + abs(Y(p) - Y(q)))


def trace(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print('func: {}\targs: {}\tkwargs: {}\tret: {}'
              .format(func.__name__, args, kwargs, ret))
        return ret
    return inner


def input1(day):
    'Read a single line value from a file'
    with open('{}_input.txt'.format(day), 'r') as f:
        return f.read().strip()


def input1_seq(f='in.txt', sep=None):
    'Read a single line seq from a file'
    return [el for el in input1(f).split(sep)]


def input_seqs(day, sep=None):
    'Read multuple line-separated seqs from a file'
    seqs = []
    with open('{}_input.txt'.format(day), 'r') as f:
        for line in f:
            seqs.append([el for el in line.strip().split()])
    return seqs


def inputs(day):
    'Read multiple line separated values'
    with open('{}_input.txt'.format(day), 'r') as f:
        return [line.strip() for line in f]


def ints(seq):
    'Cast a list of strings to ints'
    return list(map(int, seq))


def seqs_ints(seqs):
    return list(map(ints, seqs))


if __name__ == '__main__':
    assert(list(filter(partial(is_in_bounds, 0), neighbours4((0, 0)))) == [])
    assert(list(filter(partial(is_in_bounds, 4), neighbours4((0, 0)))) == [(1, 0), (0, 1)])
    print('pass')
