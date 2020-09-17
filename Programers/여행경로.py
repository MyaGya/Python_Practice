from collections import defaultdict
import heapq


def solution(tickets: [str]):
    ticket = dict

    tickets.sort(key=lambda x: x[1])
    for Lst in tickets:
        ticket[Lst[0]].append(Lst[1])

    queue = deque("ICN")

    while queue:
        data = queue.popleft()

print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN']]))
