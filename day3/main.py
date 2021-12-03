from collections import Counter

numbers = open("input.txt").read().split('\n')


def part1(numbers):
    r = [Counter(seq) for seq in zip(*numbers)]
    gamma = []
    epsilon = []
    for c in r:
        if c['1'] > c["0"]:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    gamma_num = int(''.join(gamma), 2)
    epsilon_num = int(''.join(epsilon), 2)
    return gamma_num  * epsilon_num


BIT_VALUES = {
    "oxy": ["0", "1"],
    "co2": ["1", "0"]
}

def concentration(numbers, gas):
    a, b = BIT_VALUES[gas]
    seq = numbers[:]
    bit = 0
    while len(seq) > 1:
        chars = [l[bit] for l in seq]
        c = Counter(chars)
        if c['0'] > c['1']:
            seq = [l for l in seq if l[bit] == a]
        else:
            seq = [l for l in seq if l[bit] == b]
        bit += 1
    return int(seq[0], 2)


def part2(numbers):
    print(concentration(numbers, "oxy") * concentration(numbers, "co2"))

