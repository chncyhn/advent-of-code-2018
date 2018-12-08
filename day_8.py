from collections import defaultdict


def part_1(entries):
    stack = []
    ret = 0
    n = len(entries)
    i = 0
    while i < n:
        stack.append([entries[i], entries[i + 1]])
        i += 2
        while stack and stack[-1][0] == 0:  # leaf node
            _, m = stack.pop()
            ret += sum(entries[i : i + m])
            i += m
            if stack:
                stack[-1][0] -= 1
    return ret


class Node:
    def __init__(self, c, m):
        self.c = c
        self.m = m
        self.children = []
        self.metadata = []


def get_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)

    ret = 0
    for c_i in node.metadata:
        if c_i <= len(node.children):
            c = node.children[c_i - 1]
            ret += get_value(c)
    return ret


def part_2(entries):
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
    return get_value(nodes[0])


if __name__ == "__main__":
    with open("day_8.txt") as f:
        entries = list(map(int, f.read().split(" ")))
    print(part_1(entries))
    print(part_2(entries))
