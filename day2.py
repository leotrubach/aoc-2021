with open("input2.txt") as f:
    commands = list(map(str.split, f.read().split('\n')))
    depth = 0
    position = 0
    aim = 0
    for command, sn in commands:
        n = int(sn)
        if command == "forward":
            position += n
            depth += n * aim
        elif command == "down":
            aim += n
        elif command == "up":
            aim -= n
    print(position * depth)