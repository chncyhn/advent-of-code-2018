from collections import defaultdict


def part_1(state):
    n_init = len(state)
    state = list("." * n_init + state + "." * n_init)
    new_state = ["."] * len(state)
    for _ in range(20):
        for i in range(2, len(state) - 2):
            new_state[i] = patterns[tuple(state[i - 2 : i + 3])]
        state, new_state = new_state, state
    return sum(i - n_init for i, v in enumerate(state) if v == "#")


def part_2(state):
    state_dict = defaultdict(lambda: ".")
    state_dict.update({i: v for i, v in enumerate(state)})

    n_iters = 0
    seen = set()
    new_state_dict = state_dict.copy()
    while True:
        # Find current state boundaries
        min_pot, max_pot = (
            min(state_dict, key=lambda i: (state_dict[i] != "#", i)),
            max(state_dict, key=lambda i: (state_dict[i] == "#", i)),
        )
        # Stringfy, and store if not seen.
        state_string = "".join([state_dict[i] for i in range(min_pot, max_pot + 1)])
        if state_string in seen:
            break
        seen.add(state_string)

        # Calculate new state
        for i in range(min_pot - 2, max_pot + 3):
            new_state_dict[i] = patterns[tuple(state_dict[i + j] for j in range(-2, 3))]
        state_dict, new_state_dict = new_state_dict, state_dict
        n_iters += 1

    return int(sum(i for i, v in state_dict.items() if v == "#") + (50 * 1e9 - n_iters) * 96)


if __name__ == "__main__":
    pots = {}
    with open("day_12.txt") as f:
        state = f.readline().strip()
        patterns = [p.split(" => ") for p in f.read().splitlines()]
        patterns = {tuple(p[0]): p[1] for p in patterns}
    print(f"Part 1 answer: {part_1(state)}")
    print(f"Part 2 answer: {part_2(state)}")
