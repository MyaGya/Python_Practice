from collections import defaultdict
import heapq


def solution(tickets: [str]):
    ### init ###
    route = defaultdict(list)
    for ticket in tickets:
        heapq.heappush(route[ticket[0]], ticket[1])
    for key in route.keys():
        route[key] = list(reversed(route[key]))
    stack = ["ICN"]
    ret = []
    while stack:
        top = stack[-1]
        if top not in route or len(route[top]) == 0: # 종료조건
            ret.append(stack.pop())
        else:
            stack.append(route[top][-1])
            route[top].pop()
    return(list(reversed(ret)))

print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN']]))
