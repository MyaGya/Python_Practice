ret = 0
def solution(begin, target, words):
    queue = deque()
    visited = dict()
    def check(now, s): # 일치하는지 확인
        cnt = 0
        for i in range(len(now)):
            if now[i] != s[i]:
                cnt += 1
        if 1 < cnt:
            return False
        return True
    def bfs(now, target, depth): # 너비 탐색
        if now in visited: # 재방문 방지
            return
        visited[now] = True
        if now == target: # 종료조건
            global ret
            ret = depth
            queue.clear()
            return
        for s in words:
            if check(now, s) == True:
                queue.append([s,depth+1])
        while 0 < len(queue):
            now, depth = queue.popleft()
            bfs(now, target, depth)
    bfs(begin, target, 0)
    return ret

print(solution("hit","cog",['hot', 'dot', 'dog', 'lot', 'log', 'cog']))