import numpy as np


def fuel(x, y, serial):
    rid = x + 10
    pl = rid * y
    pl += serial
    pl *= rid
    pl //= 100
    pl %= 10
    pl -= 5
    return pl


def max_window(cumsum, window_size, n):
    max_found = 0
    ans = (-1, -1)
    for x in range(n - window_size + 1):
        # Initialize window total
        window_total = sum(cumsum[x + window_size, j] - cumsum[x, j] for j in range(window_size))
        if window_total > max_found:
            max_found, ans = window_total, (x, 0)
        for y in range(1, n - window_size + 1):
            # Get new window total from the diffs
            window_total -= cumsum[x + window_size, y - 1] - cumsum[x, y - 1]
            window_total += (
                cumsum[x + window_size, y + window_size - 1] - cumsum[x, y + window_size - 1]
            )
            if window_total > max_found:
                max_found, ans = window_total, (x, y)
    return max_found, ans[0], ans[1], window_size


if __name__ == "__main__":
    serial = 4455
    n = 300
    grid = np.array([[fuel(x, y, serial) for y in range(n)] for x in range(n)])
    cumsum = np.cumsum(grid, axis=0)
    cumsum = np.insert(cumsum, 0, 0, axis=0)

    print(f"Part 1 answer: {max_window(cumsum, 3, n)[1:3]}")
    sols = [max_window(cumsum, s, n) for s in range(1, 300)]
    print(f"Part 2 answer: {max(sols)[1:]}")
