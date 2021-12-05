import math
from typing import NamedTuple
from collections import defaultdict


class Point(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    start: Point
    end: Point

    @property
    def is_horizontal(self):
        return self.start.y == self.end.y

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    def points(self):
        cur = self.start
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        l = math.sqrt(dx ** 2 + dy ** 2)
        vec_x, vec_y = (dx / l, dy / l)
        yield cur
        while cur != self.end:
            cur = Point(round(cur.x + vec_x), round(cur.y + vec_y))
            yield cur


def parse_line(line):
    start, end = line.split(" -> ")
    sx, sy = map(int, start.split(","))
    ex, ey = map(int, end.split(","))
    return Line(start=Point(sx, sy), end=Point(ex, ey))


def read_input():
    txt = open("input.txt").read()
    lines = txt.split("\n")
    return [parse_line(line) for line in lines]


def get_intersections(lines):
    bmap = defaultdict(int)
    for l in lines:
        for p in l.points():
            bmap[p.x, p.y] += 1
    count = 0
    for v in bmap.values():
        if v > 1:
            count += 1
    return count


def part1():
    all_lines = read_input()
    lines = [l for l in all_lines if l.is_vertical or l.is_horizontal]
    print(get_intersections(lines))


def part2():
    lines = read_input()
    print(get_intersections(lines))


part2()
