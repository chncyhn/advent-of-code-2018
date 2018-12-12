class Node:
    def __init__(self, c, m):
        self.c = c
        self.m = m
        self.children = []
        self.metadata = []


def parse(entries):
    nodes = []
    stack = []
    n = len(entries)
    i = 0
    while i < n:
        new = Node(entries[i], entries[i + 1])
        nodes.append(new)
        if stack:
            stack[-1].children.append(new)
        stack.append(new)
        i += 2
        while stack and stack[-1].c == 0:  # leaf node
            node = stack.pop()
            node.metadata = entries[i : i + node.m]
            i += node.m
            if stack:
                stack[-1].c -= 1
    return nodes


def get_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
        
    ret = 0
    for c_i in node.metadata:
        if c_i <= len(node.children):
            c = node.children[c_i - 1]
            ret += get_value(c)
    return ret


def get_total_metadata(nodes):
    return sum(sum(n.metadata) for n in nodes)


if __name__ == "__main__":
    with open("day_8.txt") as f:
        entries = list(map(int, f.read().split(" ")))
    nodes = parse(entries)
    print(f"Part 1 answer: {get_total_metadata(nodes)}.")
    print(f"Part 2 answer: {get_value(nodes[0])}.")
