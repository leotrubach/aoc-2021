from functools import reduce


def read_input():
    result = []
    for line in open("input.txt"):
        left, right = line.split(" | ")
        signals = left.split()
        segments = right.split()
        result.append((signals, segments))
    return result


def part1():
    counter = 0
    for _, segments in  read_input():
        for word in segments:
            if len(word) in (2, 4, 3, 7):
                counter += 1
    return counter


D2S = {

    1: 'cf',
    7: 'acf',
    4: 'bcdf',

    2: 'acdeg',
    3: 'acdfg',
    5: 'abdfg',

    6: 'abdefg',
    0: 'abcefg',
    9: 'abcdfg',

    8: 'abcdefg',
}



S2D = {
    v: k for k, v in D2S.items()
}

def decode_signals(signals):
    e2d = {k: set('abcdefg') for k in 'abcdefg'}
    for word in signals:
        possible_matches = {v for k, v in D2S.items() if len(v) == len(word)}
        pm = set(next(iter(possible_matches)))
        if len(possible_matches) == 1:
            for e in word:
                e2d[e] = e2d[e] & pm
            non_word = set('abcdefg') - set(word)
            for e in non_word:
                e2d[e] = e2d[e] - pm

    five_letters = [set(word) for word in signals if len(word) == 5]
    adg = reduce(set.intersection, five_letters)
    for e in 'abcdefg':
        if e in adg:
            e2d[e] = e2d[e] & set('adg')
        else:
            e2d[e] = e2d[e] - set('adg')

    six_letters = [set(word) for word in signals if len(word) == 6]
    abfg = reduce(set.intersection, six_letters)
    for e in 'abcdefg':
        if e in abfg:
            e2d[e] = e2d[e] & set('abfg')
        else:
            e2d[e] = e2d[e] - set('abfg')
    return {k: next(iter(v)) for k, v in e2d.items()}


def read_number(e2d, numbers):
    result = 0
    for number in numbers:
        result *= 10
        correct_segments = [e2d[c] for c in number]
        key = ''.join(sorted(correct_segments))
        result += S2D[key]
    return result


def part2():
    s = 0
    for signals, numbers in read_input():
        e2d = decode_signals(signals)
        number = read_number(e2d, numbers)
        s += number
    return s


print(part2())