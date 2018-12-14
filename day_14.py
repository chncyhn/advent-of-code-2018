def part_1(n, m):
    recipes = [3, 7]
    spots = [0, 1]
    while len(recipes) < n + m:
        new = sum(recipes[s] for s in spots)
        recipes.extend(int(i) for i in str(new))
        for i, s in enumerate(spots):
            spots[i] = (s + 1 + recipes[s]) % len(recipes)
    return "".join(str(r) for r in recipes[n : n + m])


def part_2(n):
    recipes = [3, 7]
    spots = [0, 1]
    for _ in range(int(5 * 1e7)):
        new = sum(recipes[s] for s in spots)
        recipes.extend(int(i) for i in str(new))
        for i, s in enumerate(spots):
            spots[i] = (s + 1 + recipes[s]) % len(recipes)
    target = str(n)
    recipes_string = "".join(str(r) for r in recipes)
    return recipes_string.find(target)


if __name__ == "__main__":
    n, m = 880751, 10
    print(f"Part 1 answer: {part_1(n, m)}")
    print(f"Part 2 answer: {part_2(n)}")
