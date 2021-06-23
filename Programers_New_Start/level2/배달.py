from collections import defaultdict


def solution(N, road, K):
    route = defaultdict(list)
    for source, destination, time in road:
        route[source].append((destination, time))
        route[destination].append((source, time))
    visited = {}
    stack = [(1, 0)]

    while stack:
        position, time = stack.pop()
        if time > K:
            continue
        if position in visited and visited[position] <= time:
            continue

        visited[position] = time

        for next_position, time_weight in route[position]:
            stack.append((next_position, time + time_weight))

    return len(visited.values())


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
