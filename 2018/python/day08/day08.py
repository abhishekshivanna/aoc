# in_file = 'test_input'


in_file = 'input'


class Node(object):
    def __init__(self, data, index):
        self.data = data
        self.name = index
        self.index = index
        self.num_child = self.data[self.index]
        self.num_meta = self.data[self.index + 1]
        self.index += 2
        self.children = []
        self.meta = []
        self.parse_children()

    def parse_children(self):
        for i in range(self.num_child):
            child = Node(self.data, self.index)
            self.index = child.index
            self.children.append(child)
        if self.num_meta > 0:
            self.meta = self.data[self.index:self.index + self.num_meta]
            self.index += self.num_meta

    def node_value(self):
        if not self.children:
            return sum(self.meta)
        val = 0
        for i in self.meta:
            # print("Node: {0}, meta_index: {1}".format(self.name, i))
            try:
                val += self.children[i - 1].node_value()  # grr.. 1 indexed.. should have seen this sooner.
            except:
                continue
        return val

    def print_sub_tree(self):
        print(self.name)
        for i in self.children:
            i.print_sub_tree()

    def compute_sub_tree_metadata(self):
        meta_sum = sum(self.meta)
        for i in self.children:
            meta_sum += i.compute_sub_tree_metadata()
        return meta_sum


def get_input(filename):
    with open(filename) as f:
        input_list = map(lambda x: int(x), f.read().strip().split())
    return list(input_list)


def construct_tree(inp):
    root = Node(inp, 0)
    # root.print_sub_tree()
    return root


def main():
    inp = get_input(in_file)
    root = construct_tree(inp)
    print(root.compute_sub_tree_metadata())
    print(root.node_value())


main()
