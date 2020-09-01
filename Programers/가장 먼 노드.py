from collections import defaultdict,deque

def solution(n, edge):
    ### init ###
    vertex = defaultdict(list)
    for L in edge:
        vertex[L[0]].append(L[1])
        vertex[L[1]].append(L[0])
    stack = deque()
    stack.append([1,1])
    ### calc ###
    visited = [0] * (n + 1)  # idx 0 은 사용하지 않음

    while stack:
        top, deepth = stack.popleft()
        if visited[top]:  # 방문한 노드 재방문 금지
            continue
        visited[top] = deepth
        for i in vertex[top]:
            stack.append([i, deepth + 1])
    ret = 1
    MAX = 0
    for i in range(1,n+1):
        if MAX < visited[i]:
            ret = 1
            MAX = visited[i]
        elif MAX == visited[i]:
            ret += 1
    return ret


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
