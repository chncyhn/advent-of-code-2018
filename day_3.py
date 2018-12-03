def part_1(claims):
    fabric = [[0] * 1000 for _ in range(1000)]

    for claim in claims:
        _, x, y, w, h = map(int, claim)
        for i in range(x, x + w):
            for j in range(y, y + h):
                fabric[i][j] += 1
    return sum(val > 1 for row in fabric for val in row), fabric


def part_2(fabric, claims):
    for claim in claims:
        _id, x, y, w, h = map(int, claim)
        if all(fabric[i][j] == 1 for i in range(x, x + w) for j in range(y, y + h)):
            return _id
    return -1


if __name__ == "__main__":
    with open("day_3.txt") as f:
        claims = f.read().splitlines()
        claims = [
            c.replace("#", "").replace(" @ ", ",").replace(": ", ",").replace("x", ",").split(",")
            for c in claims
        ]

    part_1_ans, fabric = part_1(claims)
    print(part_1_ans)
    print(part_2(fabric, claims))
