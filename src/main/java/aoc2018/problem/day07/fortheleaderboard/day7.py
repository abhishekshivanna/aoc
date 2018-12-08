class Dep():

    def __init__(self, name):
        self.name = name
        self.depends_on = set()

    def add_dep(self, dep):
        self.depends_on.add(dep.name)

    def is_free(self):
        return len(self.depends_on) == 0

    def remove_dep(self, dep):
        if dep.name in self.depends_on:
            self.depends_on.remove(dep.name)


dep_map = dict()

for line in open('input'):
    parts = line.split()
    second, first = parts[1], parts[7]
    first_dep = dep_map.get(first)
    if not first_dep:
        first_dep = Dep(first)
        dep_map[first] = first_dep

    second_dep = dep_map.get(second)
    if not second_dep:
        second_dep = Dep(second)
        dep_map[second] = second_dep

    first_dep.add_dep(second_dep)

done = set()


def get_next_free():
    ret = None
    possible_free = set()
    for v in dep_map.values():
        if v.name in done:
            continue
        if v.is_free():
            possible_free.add(v)

    possible_free = sorted(possible_free, key=lambda x: x.name)
    ret = possible_free[0]
    done.add(ret.name)

    for v in dep_map.values():
        v.remove_dep(ret)

    return ret.name


string = ""
while (len(done) != len(dep_map)):
    string += get_next_free()

print(string)
