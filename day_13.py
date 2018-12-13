from copy import deepcopy


class Car:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.intersection_choice = 0

    def move(self, grid, has_cars):
        has_cars[self.x][self.y] = None
        self.x += self.v[0]
        self.y += self.v[1]
        if has_cars[self.x][self.y] is not None:
            # Handle crash
            other = has_cars[self.x][self.y]
            has_cars[self.x][self.y] = None
            return False, self.x, self.y, self, other
        else:
            # Handle no crash
            has_cars[self.x][self.y] = self
            self.update_direction(grid)
            return True, self.x, self.y, None, None

    def update_direction(self, grid):
        x, y = self.x, self.y
        left = {(0, 1): (-1, 0), (0, -1): (1, 0), (1, 0): (0, 1), (-1, 0): (0, -1)}
        right = {(0, 1): (1, 0), (0, -1): (-1, 0), (1, 0): (0, -1), (-1, 0): (0, 1)}

        if grid[x][y] == "\\":
            self.v = (self.v[1], self.v[0])
        elif grid[x][y] == "/":
            self.v = (-self.v[1], -self.v[0])
        elif grid[x][y] == "+":
            if self.intersection_choice == 0:  # left
                self.v = left[self.v]
            elif self.intersection_choice == 2:  # right
                self.v = right[self.v]
            self.intersection_choice = (self.intersection_choice + 1) % 3


def part_1(cars, grid, has_cars):
    no_crash = True
    while no_crash:
        cars.sort(key=lambda c: (c.x, c.y))
        for car in cars:
            no_crash, x, y, _, _ = car.move(grid, has_cars)
            if not no_crash:
                return (y, x)


def part_2(cars, grid, has_cars):
    no_crash = True
    removed = set()
    while len(cars) > 1:
        cars.sort(key=lambda c: (c.x, c.y))
        for car in cars[:]:
            if car not in removed:
                no_crash, x, y, s, o = car.move(grid, has_cars)
                if not no_crash:
                    cars.remove(s)
                    cars.remove(o)
                    removed |= {s, o}
    return (cars[0].y, cars[0].x)


if __name__ == "__main__":
    with open("day_13.txt") as f:
        grid = [list(row) for row in f.read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    mapper = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    has_cars = [[None] * cols for _ in range(rows)]
    cars = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in ["<", ">", "^", "v"]:
                new_car = Car(i, j, mapper[grid[i][j]])
                cars.append(new_car)
                has_cars[i][j] = new_car
    print(f"Part 1 answer: {part_1(deepcopy(cars), grid, deepcopy(has_cars))}")
    print(f"Part 2 answer: {part_2(cars, grid, has_cars)}")
