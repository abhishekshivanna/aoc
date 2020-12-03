from collections import namedtuple
t = namedtuple("t", ['low', 'high', 'ch', 'password'])

with open("input") as fp:
    lines = []
    for line in fp:
        # 1-6 g: gggjgggggg
        sp = line.split()
        low, high = map(int, sp[0].split("-"))
        lines.append(t(low, high, sp[1][:-1], sp[2]))


def part1():
    c = 0
    for line in lines:
        if line.low <= line.password.count(line.ch) <= line.high:
            c += 1
    print c


def part2():
    c = 0
    for line in lines:
        valid = False
        if line.password[line.low - 1] == line.ch:
            valid = ~valid
        if len(line.password) > line.high - 1 and line.password[line.high - 1] == line.ch:
            valid = ~valid
        c += 1 if valid else 0
    print c


part1()
part2()
