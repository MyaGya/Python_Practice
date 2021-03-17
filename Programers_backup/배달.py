import heapq


def solution(N, road, K):
    distance = []

    #route = defaultdict(list)
    route = [[] for _ in range(N+1)]
    for L in road:
        route[L[0]].append([L[2], L[1]])  # route 1
        route[L[1]].append([L[2], L[0]]) # route 2

    for data in route[1]:
        heapq.heappush(distance, data)
    ret = [1]
    while distance:
        data = heapq.heappop(distance)
        if data[0] > K:                  # end case
            break
        if data[1] in ret:
            continue
        ret.append(data[1])
        for L in route[data[1]]:
            heapq.heappush(distance,[data[0]+L[0],L[1]])
    return len(ret)

print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
