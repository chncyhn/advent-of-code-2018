from collections import Counter


def part_1(words):
    counters = [Counter(w) for w in words]
    two_letters_num = sum([any(v == 2 for v in c.values()) for c in counters])
    three_letters_num = sum([any(v == 3 for v in c.values()) for c in counters])
    return two_letters_num * three_letters_num


def part_2(words):
    def has_only_1_diff(w0, w1):
        found_diff = False
        for x, y in zip(w0, w1):
            if x != y:
                if found_diff:
                    return False
                else:
                    found_diff = True
        return True

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if has_only_1_diff(words[i], words[j]):
                return "".join([x for x, y in zip(words[i], words[j]) if x == y])


if __name__ == "__main__":
    with open("day_2.txt") as f:
        words = f.read().splitlines()
    print(part_1(words))
    print(part_2(words))
