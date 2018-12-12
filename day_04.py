from collections import defaultdict
from datetime import datetime, timedelta


def preprocess(events):
    events.sort()

    guard_minute_sleep = defaultdict(lambda: defaultdict(int))
    cur_guard = -1
    for i, event in enumerate(events):
        if event[1] == "begin":
            cur_guard = event[2]
        elif event[1] == "wake":
            sleep_time, wake_time = events[i - 1][0], event[0]
            while sleep_time < wake_time:
                guard_minute_sleep[cur_guard][sleep_time.minute] += 1
                sleep_time += timedelta(minutes=1)
    return guard_minute_sleep


def part_1(guard_minute_sleep):
    most_sleeping_guard = max(guard_minute_sleep, key=lambda g: sum(guard_minute_sleep[g].values()))
    most_slept_minute = max(
        guard_minute_sleep[most_sleeping_guard],
        key=lambda m: guard_minute_sleep[most_sleeping_guard][m],
    )
    return int(most_sleeping_guard) * most_slept_minute


def part_2(guard_minute_sleep):
    most_freq_guard, most_freq_minute = max(
        [(guard, minute) for guard in guard_minute_sleep for minute in guard_minute_sleep[guard]],
        key=lambda x: guard_minute_sleep[x[0]][x[1]],
    )
    return int(most_freq_guard) * most_freq_minute


if __name__ == "__main__":
    with open("day_4.txt") as f:
        inp = [i.replace("[", "").replace("]", "").replace("#", "") for i in f.read().splitlines()]

    events = []
    for event in inp:
        if event.endswith("begins shift"):
            date, t, _, guard, _, _ = event.split(" ")
            events.append((datetime.strptime(date + " " + t, "%Y-%m-%d %H:%M"), "begin", guard))
        elif event.endswith("falls asleep"):
            date, t, _, _ = event.split(" ")
            events.append((datetime.strptime(date + " " + t, "%Y-%m-%d %H:%M"), "sleep"))
        else:
            date, t, _, _ = event.split(" ")
            events.append((datetime.strptime(date + " " + t, "%Y-%m-%d %H:%M"), "wake"))

    guard_minute_sleep = preprocess(events)
    print(part_1(guard_minute_sleep))
    print(part_2(guard_minute_sleep))
