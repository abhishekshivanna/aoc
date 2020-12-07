from collections import defaultdict

with open("input") as fp:
    lines = [line for line in fp]


def fIndex():
    index = {}
    for line in lines:
        parts = line.split()
        outer = " ".join(parts[:2])
        i = 2
        inner = {}
        while i < len(parts):
            if parts[i].isdigit():
                inner[" ".join(parts[i+1:i+3])] = int(parts[i])
                i += 3
            else:
                i += 1
        index[outer] = inner
    return index


def rIndex():
    forwardIndex = fIndex()
    reverseIndex = defaultdict(set)
    for k, v in forwardIndex.items():
        for bag in v.keys():
            reverseIndex[bag].add(k)

    return reverseIndex


def part1():
    output = set()
    reverseIndex = rIndex()

    def count(bag):
        bags = reverseIndex.get(bag)
        if not bags:
            return
        for b in bags:
            output.add(b)
            count(b)

    count("shiny gold")
    print(len(output))


def part2():
    output = 0
    forwardIndex = fIndex()

    def count(bag):
        if not forwardIndex[bag]:
            return 0
        c = 0
        for k, v in forwardIndex.get(bag).items():
            c += v + (count(k) * v)
        return c

    for bag, c in forwardIndex.get("shiny gold").items():
        output += c + (count(bag) * c)

    print(output)


part1()
part2()
