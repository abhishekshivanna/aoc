from collections import deque

# in_file = 'test_input'
in_file = 'input'


def part1(num_players, num_marbles):
    elf_score = dict()
    marbles = deque()
    marbles.append(0)
    current_elf = 1
    for current_marble in range(1, num_marbles + 1):
        if current_marble % 23 == 0:
            marbles.rotate(-7)
            score = current_marble + marbles.pop()
            if current_elf in elf_score:
                elf_score[current_elf] += score
            else:
                elf_score[current_elf] = score
        else:
            marbles.rotate(2)
            marbles.append(current_marble)
        current_elf = (current_elf + 1) % num_players
    return max(elf_score.values())


def part2(num_players, num_marbles):
    return part1(num_players, num_marbles * 100)


def get_input(in_file):
    with open(in_file) as f:
        content = f.read().strip().split()
        return (int(content[0]), int(content[6]))


def main():
    num_players, num_marbles = get_input(in_file)
    # print(num_players, num_marbles)
    print(part1(num_players, num_marbles))
    print(part2(num_players, num_marbles))


main()
