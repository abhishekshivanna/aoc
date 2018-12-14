inp = 702831


def compute(recipe, elf1_idx, elf2_idx):
    new_recipe = 0

    elf1_cur_recipe = recipe[elf1_idx]
    new_recipe += elf1_cur_recipe

    elf2_cur_recipe = recipe[elf2_idx]
    new_recipe += elf2_cur_recipe

    for i in str(new_recipe):
        recipe.append(int(i))

    elf1_idx = (elf1_idx + elf1_cur_recipe + 1) % len(recipe)
    elf2_idx = (elf2_idx + elf2_cur_recipe + 1) % len(recipe)

    return recipe, elf1_idx, elf2_idx


def part1():
    recipe = [3, 7]
    elf1_idx = 0
    elf2_idx = 1
    while len(recipe) < inp + 10:
        recipe, elf1_idx, elf2_idx = compute(recipe, elf1_idx, elf2_idx)
    print(recipe[-10:])


def part2():
    recipe = [3, 7]
    inp_list = [7, 0, 2, 8, 3, 1]
    elf1_idx = 0
    elf2_idx = 1
    while True:
        recipe, elf1_idx, elf2_idx = compute(recipe, elf1_idx, elf2_idx)
        if recipe[-6:] == inp_list or recipe[-7:-1] == inp_list:
            print(len(recipe) - 6, len(recipe) - 7)
            break


def main():
    part1()
    part2()


main()
