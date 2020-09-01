# 중복 케이스 해결 불가
from collections import defaultdict
import heapq


def dfs(depart, route: dict, history: list, have_ticket):
    history.append(depart)
    if len(history) == have_ticket:
        return True
    for _ in reversed(route[depart]):
        L = route[depart][-1]
        if dfs(L, route, history, have_ticket):
            return True
    history.pop()
    return False


def solution(tickets: [str]):
    # init
    route = defaultdict(list)
    for L in tickets:
        depart, arrival = L
        heapq.heappush(route[depart], arrival)
    for key in route.keys():
        route[key] = list(reversed(route[key]))
    # find history
    ret = []
    dfs("ICN", route, ret, len(tickets) + 1)
    return (ret)


print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN']]))
