import collections
from itertools import tee, islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def part1():
    with open("input1.txt") as f:
        INPUT = map(int, f.read().split())
        count = 0
        for p, n in pairwise(INPUT):
            if n > p:
                count += 1

        print(count)


def part2():
    with open("input1.txt") as f:
        INPUT = map(int, f.read().split())
        count = 0
        for p, n in pairwise(sliding_window(INPUT, 3)):
            if sum(n) > sum(p):
                count += 1

        print(count)

part1()