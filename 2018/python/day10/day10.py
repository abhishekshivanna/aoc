import re

# in_file = 'test_input'
in_file = 'input'


def get_input(in_file):
    points = []
    velocity = []
    with open(in_file) as f:
        for line in f:
            splits = re.findall("-?\d+", line)
            # print(splits)
            points.append((int(splits[0]), int(splits[1])))
            velocity.append((int(splits[2]), int(splits[3])))
    return points, velocity


def compute_area_of_positive_grid(points):
    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])
    return max_x * max_y


def compute_grid(points, should_print=False):
    min_x = min([point[0] for point in points])
    max_x = max([point[0] for point in points])
    min_y = min([point[1] for point in points])
    max_y = max([point[1] for point in points])

    grid_offset = (min_x, min_y)

    offset_points = []
    for point in points:
        offset_points.append((point[0] - grid_offset[0], point[1] - grid_offset[1]))

    grid_area = compute_area_of_positive_grid(offset_points)

    if should_print:
        grid = [['-' for _ in range(max_y - min_y + 1)] for _ in range(max_x - min_x + 1)]
        for point in offset_points:
            grid[point[0]][point[1]] = '#'
        for y in range(max_y - min_y + 1):
            row = []
            for x in range(max_x - min_x + 1):
                row.append(str(grid[x][y]))
            print(" ".join(row))
        print("")

    return grid_area


def mutate_points(points, velocity, reverse=False):
    mutated_points = []
    for i in range(len(points)):
        if reverse:
            mutated_points.append((points[i][0] - velocity[i][0], points[i][1] - velocity[i][1]))
        else:
            mutated_points.append((points[i][0] + velocity[i][0], points[i][1] + velocity[i][1]))
    return mutated_points


def solve(points, velocity):
    current_area = compute_grid(points)
    previous_area = 999999999999
    iterations = 0
    while current_area < previous_area:
        iterations += 1
        previous_area = current_area
        points = mutate_points(points, velocity)
        current_area = compute_grid(points)

    points = mutate_points(points, velocity, reverse=True)
    compute_grid(points, should_print=True)
    print(iterations - 1)


def main():
    points, velocity = get_input(in_file)
    solve(points, velocity)


main()
