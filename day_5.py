from string import ascii_lowercase


def part_1(polymer):
    stack = []
    for p in polymer:
        if stack and abs(ord(p) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(p)
    return len(stack)


def part_2(polymer):
    results = {}
    for l in ascii_lowercase:
        results[l] = part_1([p for p in polymer if p not in [l, l.upper()]])
    return min(results.values())


if __name__ == "__main__":
    with open("day_5.txt") as f:
        polymer = list(f.read())
    print(part_1(polymer))
    print(part_2(polymer))

