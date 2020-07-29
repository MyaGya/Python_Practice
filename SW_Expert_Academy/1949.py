# 테스트 1번, 등산로 조성

# 테스트 케이스
T = int(input())

global N, K
global visited
global data
global result

# 방향 전환
def Direct(i, j, number):
    if number == 0:
        return i - 1, j
    elif number == 1:
        return i, j - 1
    elif number == 2:
        return i + 1, j
    else:
        return i, j + 1

def DFS_init(i, j, depth, hight, useDig):
    for direction in range(4):
        visited[i][j] = True
        new_i, new_j = Direct(i, j, direction)
        DFS(new_i, new_j, depth + 1, hight, useDig)
        visited[i][j] = False

# 탐색 함수
'''
i : 위치
j : 위치
depth : 깊이
hight : 높이
useDig : False or True
'''
def DFS(i, j, depth, hight, useDig):
    global result
    # 예외조건
    if i < 0 or j < 0 or N <= i or N <= j or visited[i][j]:
        result = max(result, depth-1)
        return -1

    # 종료조건

    # 현재 위치가 조건과 일치하지 않는가?
    if data[i][j] >= hight:
        # 땅 파기를 사용한 경우
        if useDig:
            result = max(result, depth)
            return -1
        # 땅을 파도 도달 할 수 없는 경우
        elif data[i][j] - K > hight:
            result = max(result, depth)
            return -1

        # 땅파기를 사용해서 도달 할 수 있는 경우
        else:
            # 네 방향 확인 (땅파기 사용)
            for direction in range(4):
                visited[i][j] = True
                data[i][j] =
                new_i, new_j = Direct(i, j, direction)
                DFS(new_i, new_j, depth + 1, data[i][j], True)
                visited[i][j] = False
    # 네 방향 확인 (땅파기 미사용)
    for direction in range(4):
        visited[i][j] = True
        new_i, new_j = Direct(i, j, direction)
        DFS(new_i, new_j, depth + 1, data[i][j], useDig)
        visited[i][j] = False



for testCase in range(1, T + 1):
    # 최종 결과값
    global result
    result = 0
    # N : 지도 한 변의 길이
    # K : 최대 공사 가능 깊이
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    # 최대값 찾기
    Max = 0
    for i in range(N):
        for j in range(N):
            Max = max(Max, data[i][j])

    # 최대 위치에서 연산 진행
    for i in range(N):
        for j in range(N):
            if data[i][j] == Max:

                DFS_init(i, j, 1, Max, False)
    print("#%d %d"%(testCase, result))