from collections import defaultdict


def solution(tickets: [str]):
    n = len(tickets)
    ### init ###
    route = defaultdict(list)
    visited = defaultdict(int )
    tickets.sort(key=lambda x: x[1])

    for ticket in tickets:
        route[ticket[0]].append(ticket[1])
    for ticket in route:
        visited[ticket] = len(route[ticket])
    print(visited)
    ret = ["ICN"]

    def dfs(starting):  # 목적지를 기준으로 반복

        if len(ret) == n+1:  # 종료 조건
            return True
        if visited[starting] <=0:  # 티켓보다 많이 방문했을 경우 종료
            return False

        visited[starting] -= 1
        for ticket in route[starting]:
            ret.append(ticket)
            if dfs(ticket):
                return True
            ret.pop()
        visited[starting] += 1

    dfs("ICN")
    return ret

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
