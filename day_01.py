def part_1(freq_changes):
    return sum(freq_changes)


def part_2(freq_changes):
    seen = {0}
    i, cur = 0, 0
    while True:
        cur += freq_changes[i]
        if cur in seen:
            return cur
        else:
            seen.add(cur)
            i = (i + 1) % len(freq_changes)


if __name__ == "__main__":
    with open("day_1.txt") as f:
        freq_changes = list(map(int, f.readlines()))
    print(part_1(freq_changes))
    print(part_2(freq_changes))
