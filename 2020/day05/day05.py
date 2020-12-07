with open("input") as fp:
    lines = [line.strip() for line in fp]


def binSearch(s, low, high, lch, hch):
    for ch in s:
        mid = low + (high - low) / 2
        if ch == lch:
            high = mid
        else:
            low = mid + 1
    return low


def getSeats():
    seats = []
    for line in lines:
        row = binSearch(line[:7], 0, 127, 'F', 'B')
        col = binSearch(line[7:], 0, 7, 'L', 'R')
        seats.append(row * 8 + col)
    return seats


def part1():
    seats = getSeats()
    print(max(seats))


def part2():
    seats = getSeats()
    print(set(range(min(seats), max(seats))) - set(sorted(seats)))


part1()
part2()
