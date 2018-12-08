
from collections import Counter
size = 500
inp = 'input'
part2_size = 10000

# size = 10
# inp = 'test_input'
# part2_size = 32

def build_grid():
    grid = []
    for x in range(size):
        li = []
        for y in range(size):
            li.append({'marker': 0, 'dist': 99999999999, 'tot_dist': 0})
        grid.append(li)
    return grid

def get_input(filename):
    points = []
    with open(filename) as f:
        for line in f:
            y, x = line.split(", ")
            points.append((int(x.strip()), int(y.strip())))

    return points

def insert_points(points, grid):
    marker = 1
    for x, y in points:
        grid[x][y] = {'marker': marker, 'dist': 0, 'tot_dist': 0}
        marker += 1

    return grid

def manhattan_distance(src, dest):
    return abs(src[0] - dest[0]) + abs(src[1] - dest[1])


def compute(point, grid, marker):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            dist = manhattan_distance(point, (x, y))
            grid[x][y]['tot_dist'] += dist
            if dist < grid[x][y]['dist']:
                grid[x][y]['marker'] = marker
                grid[x][y]['dist'] = dist
            if dist == grid[x][y]['dist'] and grid[x][y]['marker'] != marker:
                grid[x][y]['marker'] = '.'

def border_markers(grid):
    border = set()
    for x in range(len(grid)): # left
        border.add(grid[x][0]['marker'])
    for x in range(len(grid)): # top
        border.add(grid[0][x]['marker'])

    for x in range(len(grid)): # right
        border.add(grid[x][len(grid)-1]['marker'])
    for x in range(len(grid)): # bottom
        border.add(grid[len(grid)-1][x]['marker'])

    return border


def print_grid(grid, key='marker'):
    for x in range(len(grid)):
        row = []
        for y in range(len(grid[x])):
            row.append(str(grid[x][y][key]))
        print(row)
    print("")


def count_grids_for_point(grid):
    c = Counter([])
    for row in grid:
        c.update(map(lambda x: x['marker'], row))
    return c


def part1(grid):
    # print_grid(grid)
    counts = count_grids_for_point(grid)
    # print(counts)
    border = border_markers(grid)
    # print(border)

    for b in border:
        counts.pop(b)

    # print(counts)
    return max(counts.values())

def part2(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]['tot_dist'] < part2_size:
                count += 1
    return count


def main():
    points = get_input(inp)
    grid = build_grid()
    insert_points(points, grid)
    # print_grid(grid)
    for point in points:
        compute(point, grid, grid[point[0]][point[1]]['marker'])
        # print_grid(grid)
    print(part1(grid))
    print(part2(grid))

main()