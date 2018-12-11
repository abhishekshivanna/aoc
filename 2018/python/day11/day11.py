class Node(object):
    def __init__(self, x, y, serial):
        self.x = x
        self.y = y
        self.serial = serial
        self.power_level = self.rackId * self.y
        self.compute_power()

    @property
    def rackId(self):
        return self.x + 10

    def dec_power(self, val=1):
        self.power_level -= val

    def inc_power(self, val=None):
        if not val:
            self.power_level += self.serial
        else:
            self.power_level += val
        self.power_level *= self.rackId

    def compute_power(self):
        self.inc_power()
        if self.power_level > 100:
            self.power_level = (self.power_level // 100) % 10
        else:
            self.power_level = 0
        self.power_level -= 5


def construct_grid(serial):
    grid = []
    for y in range(300):
        row = []
        for x in range(300):
            row.append(Node(x, y, serial))
        grid.append(row)
    return grid


def print_grid(grid):
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[y])):
            row.append(str(grid[y][x].power_level))
        print(row)
    print("")


def compute_value(x, y, grid, size=3):
    sum = 0
    for xx in range(x, x + size):
        for yy in range(y, y + size):
            if xx == len(grid) or yy == len(grid):
                return -99999999
            # print(x, y)
            sum += grid[xx][yy].power_level
    return sum


def find_maxima(grid, size=3):
    max_x = -1
    max_y = -1
    max_value = -999999999
    for y in range(len(grid)):
        for x in range(len(grid)):
            value = compute_value(y, x, grid, size)
            if max_value < value:
                max_value = value
                max_x = x
                max_y = y
    return max_value, max_x, max_y


def part1(serial):
    grid = construct_grid(serial)
    # print(compute_value(45, 33, grid))
    print(find_maxima(grid))


def part2(serial):
    current_maxima = (0, 0, 0)
    current_max_size = 0
    grid = construct_grid(serial)
    for size in range(3, 300):
        maxima = find_maxima(grid, size=size)
        if maxima[0] > current_maxima[0]:
            current_maxima = maxima
            current_max_size = size
            print(current_maxima)
            print(current_max_size)
            print("")

    print(current_maxima)
    print(current_max_size)


def main():
    serial = 9435
    # serial = 18
    part1(serial)
    part2(serial)


main()
