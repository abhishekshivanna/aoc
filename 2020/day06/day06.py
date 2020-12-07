with open("input") as fp:
    lines = fp.read()
    groups = lines.split("\n\n")
    group_ans = [''.join(group.split()) for group in groups]


def part1():
    count = 0
    for ans in group_ans:
        count += len(set(ans))
    print(count)


def part2():
    count = 0
    for group in groups:
        s = set.intersection(*[set(g) for g in group.split()])
        count += len(s)
    print(count)


part1()
part2()
