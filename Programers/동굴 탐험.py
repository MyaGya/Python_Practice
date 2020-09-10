from collections import defaultdict, deque


def solution(n, path, order):
    queue = deque()  # [int,int...] 전체 반복
    waitting = deque() # [int,int...] 조건에 걸린 위치 임시 대기
    data = defaultdict(list)
    visited = dict()
    pre_visit = dict()

    for L in path:               # 기초 경로 입력
        data[L[0]].append(L[1])
        data[L[1]].append(L[0])
    for L in order:              # 사전 방문 경로 입력
        pre_visit[L[1]] = L[0]


    queue.append(0)
    flag = False  # 한 번이라도 방문했다면 True가 된다
    while queue:
        value = queue.popleft()
        
        if not queue and flag:  # 큐가 비었다면 대기중인 값들을 넣어준다
            queue = waitting
            waitting = deque()
            flag = False

        if value in visited:  # 재방문 금지
            continue
        if value in pre_visit and pre_visit[value] not in visited:  # 사전 탐색 경로가 있을경우
            # 해당 경로를 방문하지 않았다면 대기
            waitting.append(value)
            continue
        visited[value] = True # 방문
        flag = True
        for i in data[value]:
            queue.append(i)


    if waitting: #  기다리고 있는 값이 있으면
        return False
    return True
print(solution(9,[[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]))
