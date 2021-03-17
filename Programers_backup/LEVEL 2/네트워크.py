def dfs(n, computers, visited):
    if visited[n]:
        return
    visited[n] = True
    for i in range(len(computers)):
        if computers[n][i] and n != i:
            dfs(i,computers,visited)

def solution(n, computers):
    visited = [False] * n
    ret = 0
    for i in range(n):
        if not visited[i]:
            dfs(i,computers,visited)
            ret += 1
    return ret


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
