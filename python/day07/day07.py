in_file = 'input'
# in_file = 'test_input'


class Node(object):
    def __init__(self, name):
        self.name = name
        self.depends_on = []
        self.blocks = []
        self.done = False
        self.value = ord(name) - 4  # 64
        self.is_worked_on = False

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)

    def add_dependency(self, node):
        self.depends_on.append(node)

    def add_block(self, node):
        self.blocks.append(node)

    def remove_dependency(self, node):
        self.depends_on.remove(node)

    def remove_block(self, node):
        self.blocks.remove(node)

    def mark_done(self):
        self.done = True

    def do_task(self, tick=1):
        self.value -= tick
        if self.value == 0:
            self.done = True

    def is_done(self):
        return self.done


class Graph(object):
    def __init__(self):
        self.nodes = dict()

    def get_nodes(self):
        return self.nodes

    def add_node(self, node):
        self.nodes[node] = node

    def add_dependency_edge(self, src, dest):
        if not self.nodes.get(src):
            temp = Node(src)
            self.nodes[temp] = temp
        if not self.nodes.get(dest):
            temp = Node(dest)
            self.nodes[temp] = temp
        self.nodes.get(src).add_dependency(dest)
        self.nodes.get(dest).add_block(src)

    def get_free_nodes(self):
        free_nodes = []
        for node in self.nodes.values():
            if len(node.depends_on) == 0 and not node.done and not node.is_worked_on:
                free_nodes.append(node)
        return sorted(free_nodes, key=lambda x: x.name)

    def mark_node_as_done(self, node):
        for i in self.nodes[node].blocks:
            self.nodes[i].remove_dependency(node)
        self.nodes[node].blocks = []
        self.nodes[node].mark_done()


class WorkCoordinator(object):
    def __init__(self, graph, num_workers):
        self.workers = list()
        self.graph = graph
        self.time = 0
        for i in range(num_workers):
            self.workers.append({"name": i, "isFree": True, "currentTask": None})

    def assign_work(self, task):
        for worker in self.workers:
            if worker['isFree']:
                worker['currentTask'] = task
                return True
        return False

    def assign_work_if_needed(self):
        for worker in self.workers:
            if worker['currentTask'] and worker['currentTask'].is_done():
                self.graph.mark_node_as_done(worker['currentTask'])
                worker['currentTask'] = None
                worker['isFree'] = True

        free_tasks = self.graph.get_free_nodes()
        if not free_tasks:
            return

        i = 0
        for worker in self.workers:
            if worker['isFree'] and free_tasks:
                worker['currentTask'] = free_tasks[i]
                free_tasks[i].is_worked_on = True
                worker['isFree'] = False
                i += 1
                if i == len(free_tasks):
                    break

    def tick(self):
        self.assign_work_if_needed()
        self.time += 1
        for worker in self.workers:
            if not worker['isFree']:
                worker['currentTask'].do_task()
                # print("currentTime:{2}, Node: {0}, remaining: {1}, worker:{3}".format(worker['currentTask'].name,
                #                                                 worker['currentTask'].value, self.time, worker['name']))


def construct_graph(inp):
    graph = Graph()
    for node in inp:
        graph.add_dependency_edge(node[0], node[1])
    return graph


def get_input(filename):
    with open(filename) as f:
        input_list = [(line.split()[7], line.split()[1]) for line in f]
    return input_list


def part1(inp):
    order = []
    graph = construct_graph(inp)
    while True:
        free_nodes = graph.get_free_nodes()
        if not free_nodes:
            break
        order.append(free_nodes[0])
        graph.mark_node_as_done(free_nodes[0])

    return "".join([o.name for o in order])


def part2(inp):
    graph = construct_graph(inp)
    wc = WorkCoordinator(graph, 5)
    done = False
    while not done:
        wc.tick()
        done = all([node.is_done() for node in graph.nodes])
    return wc.time


def main():
    inp = get_input(in_file)
    print(part1(inp))
    print(part2(inp))


main()
