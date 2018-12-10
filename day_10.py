class Point:
    def __init__(self, x, v):
        self.x = list(map(int, x))
        self.v = list(map(int, v))

    def is_neighbour(self, other):
        return abs(other.x[0] - self.x[0]) + abs(other.x[1] - self.x[1]) <= 1

    def has_neighbour(self, pts):
        for pt in pts:
            if self.is_neighbour(pt) and self != pt:
                return True
        return False

    def move(self):
        self.x[0] += self.v[0]
        self.x[1] += self.v[1]


def print_points(pts):
    min_coord = min(c for p in pts for c in p.x)
    max_coord = max(c for p in pts for c in p.x)

    n = max_coord - min_coord + 2
    grid = [[" "] * n for _ in range(n)]
    for pt in pts:
        grid[pt.x[1] - min_coord][pt.x[0] - min_coord] = "#"
    for row in grid:
        print(*row)


if __name__ == "__main__":
    with open("day_10.txt") as f:
        pts = f.read().splitlines()
        pts = [
            x.split(", ")
            for p in pts
            for x in p.replace("position=", "").replace("<", "").replace(">", "").split("velocity=")
        ]
        pts = [Point(x, v) for x, v in zip(pts[::2], pts[1::2])]

    i = 0
    while True:
        i += 1
        for pt in pts:
            pt.move()
        if i == 10710:
            print("-" * 75)
            print(i)
            print_points(pts)
            break
