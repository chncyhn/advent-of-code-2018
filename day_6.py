from scipy.spatial import KDTree
from collections import defaultdict
from itertools import product


def part_1(coords):
    n = 400
    grid = [[0] * n for _ in range(n)]
    kd = KDTree(coords)

    query_points = [(i, j) for i in range(n) for j in range(n)]
    d, nn = kd.query(query_points, k=2, p=1)
    nn[:, 0][d[:, 0] == d[:, 1]] = -1  # mark if equality
    nn = nn[:, 0]  # select closest neighbour
    for i, j in product(range(n), range(n)):
        grid[i][j] = nn[i * n + j]

    infs = set()
    for i in [0, n - 1]:
        for j in range(n):
            infs.add(grid[i][j])
    for i in range(n):
        for j in [0, n - 1]:
            infs.add(grid[i][j])

    areas = defaultdict(int)
    for i, j in product(range(n), range(n)):
        if grid[i][j] != -1 and grid[i][j] not in infs:
            areas[grid[i][j]] += 1
    return max(areas.values())


def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_2(coords, d_threshold=10000):
    n = 400
    grid = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for coord in coords:
                grid[i][j] += manhattan_dist((i, j), coord)
                if grid[i][j] > d_threshold:
                    break
    return sum(grid[i][j] < d_threshold for i in range(n) for j in range(n))


if __name__ == "__main__":
    with open("day_6.txt") as f:
        coords = [tuple(map(int, coord.split(","))) for coord in f.read().splitlines()]
    print(part_1(coords))
    print(part_2(coords))
