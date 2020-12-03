grid = []

with open("input") as fp:
    for line in fp:
        grid.append(line.strip())


def part1(right=3, down=1):
    col = 0
    trees = 0
    for row in range(0, len(grid), down):
        if grid[row][col] == "#":
            trees += 1
        col = (col + right) % len(grid[row])
    return trees


def part2():
    dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    out = 1
    for right, down in dirs:
        out *= part1(right, down)
    return out


print(part1())
print(part2())
