import itertools

with open("input") as fp:
    lines = [int(l) for l in fp]


def part1():
    twoSum = {}
    for line in lines:
        if line in twoSum:
            print(line * twoSum[line])
            return
        else:
            twoSum[2020-line] = line


def part2():
    line_set = set(lines)
    for i in itertools.combinations(lines, 2):
        check = 2020 - (i[0] + i[1])
        if check in line_set:
            print(i[0] * i[1] * check)
            return


part1()
part2()
