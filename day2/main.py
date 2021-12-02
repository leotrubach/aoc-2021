def part2(commands):
    depth = 0
    position = 0
    aim = 0
    for command, n in commands:
        if command == "forward":
            position += n
            depth += n * aim
        elif command == "down":
            aim += n
        elif command == "up":
            aim -= n
    return depth * position


def part1(commands):
    depth = 0
    position = 0
    for command, n in commands:
        if command == "forward":
            position += n
        elif command == "down":
            depth += n
        elif command == "up":
            depth -= n
    return depth * position


with open("input2.txt") as f:
    commands = [(c, int(v)) for c, v in map(str.split, f.read().split('\n'))]
    print(part1(commands))
    print(part2(commands))