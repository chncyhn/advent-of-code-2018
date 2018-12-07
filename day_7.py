from collections import defaultdict
from heapq import heappop, heappush, heapify
from copy import deepcopy


def part_1(graph, preqs):
    all_nodes, ret = preqs.keys() | graph.keys(), []
    pq = [node for node in all_nodes if len(preqs[node]) == 0]
    heapify(pq)
    while pq:
        cur = heappop(pq)
        ret.append(cur)
        for nxt in graph[cur]:
            preqs[nxt].remove(cur)
            if len(preqs[nxt]) == 0:
                heappush(pq, nxt)
    return "".join(ret)


def part_2(graph, preqs, t_fixed=60, num_workers=5):
    all_nodes = preqs.keys() | graph.keys()
    available_workers = num_workers

    available_jobs = [node for node in all_nodes if len(preqs[node]) == 0]
    heapify(available_jobs)
    # Initialize event queue
    event_queue = []
    while available_workers > 0 and available_jobs:
        job = heappop(available_jobs)
        available_workers -= 1
        event_queue.append((t_fixed + ord(job) - 64, job))

    while event_queue:
        t, job = heappop(event_queue)
        available_workers += 1
        # Update available jobs
        for nxt in graph[job]:
            preqs[nxt].remove(job)
            if len(preqs[nxt]) == 0:
                heappush(available_jobs, nxt)
        # Disperse if there are pending jobs & available workers
        while available_workers > 0 and available_jobs:
            nxt = heappop(available_jobs)
            available_workers -= 1
            heappush(event_queue, (t + t_fixed + ord(nxt) - 64, nxt))
    return t


if __name__ == "__main__":
    graph = defaultdict(set)
    preqs = defaultdict(set)
    with open("day_7.txt") as f:
        ins = [i.split(" ") for i in f.read().splitlines()]
        ins = [(i[1], i[-3]) for i in ins]
    for i in ins:
        u, v = i
        graph[u].add(v)
        preqs[v].add(u)
    print(part_1(graph, deepcopy(preqs)))
    print(part_2(graph, preqs, 60, 5))
