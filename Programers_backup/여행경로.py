from collections import defaultdict


def dfs(depart, route, route_count, ticket_count, history):
    '''
    depart : 출발지
    destination : 도착지
    route : 가능한 경로
    route_count : 가능한 경로의 갯수
    ticket_count : 남은 티켓 갯수
    history : 지나온 경로
    '''

    history.append(depart)  # 지나온 경로 추가

    if not ticket_count:  # end cond
        return True

    for destination in route[depart]:
        if route_count[tuple((depart, destination))]:
            route_count[tuple((depart, destination))] -= 1
            if dfs(destination, route, route_count, ticket_count-1, history):
                return True
            route_count[tuple((depart, destination))] += 1

    history.pop()  # 지나온 경로 해제
    return False

def solution(tickets):
    # 다시 돌아왔다 가는 경로도 생각해야한다. 즉, 특정 위치에서 다른 위치로 몇 번이나 갈 수 있는지를 체크해야한다
    route_count = defaultdict(int)
    route = defaultdict(set)
    ticket_count = len(tickets)

    for ticket in tickets:
        route_count[tuple(ticket)] += 1
        route[ticket[0]].add(ticket[1])

    for key in route.keys():                    # 사전순으로 탐색
        route[key] = sorted(list(route[key]))
    ret = []
    dfs("ICN", route, route_count, ticket_count,ret)
    return ret

print(solution([['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]))
