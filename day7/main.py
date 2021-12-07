def read_input():
    return list(map(int, open("input.txt").read().split(",")))


def distance(positions, centroid):
    return sum(abs(p - centroid) for p in positions)


def distance2(positions, centroid):
    r = 0
    for p in positions:
        ds = abs(p - centroid)
        dss = ds * (ds + 1) / 2
        r += dss
    return r


def estimate(positions, centroid):
    a = sum(p / abs(p - centroid) for p in positions)
    b = sum(1 / abs(p - centroid) for p in positions)
    return a / b


def estimate2(positions, centroid):
    a = 0
    b = 0
    for p in positions:
        ds = abs(p - centroid)
        dss = ds * (ds + 1) / 2
        a += p / dss
        b += 1 / dss
    return a / b


def part1():
    positions = read_input()
    centroid = sum(positions) / len(positions)
    while True:
        new_centroid = estimate(positions, centroid)
        if abs(new_centroid - centroid) < 0.01:
            break
        centroid = new_centroid
    return distance(positions, int(centroid))


def part2():
    positions = read_input()
    return min(distance2(positions, int(p)) for p in range(min(positions), max(positions) + 1))



print(part2())
