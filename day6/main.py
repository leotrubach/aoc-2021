from collections import Counter, defaultdict
from typing import List


def read_input():
    return list(map(int, open("input.txt").read().split(',')))


def simulate(d: dict):
    new = defaultdict(int)
    for days, count in d.items():
        if days > 0:
            new[days - 1] += count
        else:
            new[6] += count
            new[8] = count
    return new

def part1(data: List[int]):
    c = Counter(data)
    d = c
    for _ in range(80):
        d = simulate(d)
    return sum(d.values())


def part2(data: List[int]):
    c = Counter(data)
    d = c
    for _ in range(256):
        d = simulate(d)
    return sum(d.values())


print(part2(read_input()))