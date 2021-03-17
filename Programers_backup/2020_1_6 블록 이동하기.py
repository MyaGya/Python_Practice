# X와 Y축을 거꾸로 생각하고 풀었다. board[X축][Y축]이라고 생각해버림. 결과적으로는 큰 차이 없었지만 주의 할 것
import collections
import sys

# 초기값 및 최대값
sys.setrecursionlimit(10 ** 8)  # 10^8 까지 늘림.


def BFS(board, visited, que, X, Y, option, depth):
    # 예외 조건
    if X < 0 or Y < 0 or X > len(board) - 1 or Y > len(board) - 1 or (option == 0 and X > len(board) - 2) or (
            option == 1 and Y > len(board) - 2) or visited[X][Y][option] != -1:
        return -1
    if option == 0:
        if board[X][Y] == 1 or board[X+1][Y] == 1:
            return -1
    if option == 1:
        if board[X][Y] == 1 or board[X][Y+1] == 1:
            return -1
    # 종료 조건
    if (X == len(board)-2 and Y == len(board)-1 and option == 0) or (X == len(board) -1 and Y == len(board)-2 and option == 1):
        que.clear()
        return depth

    visited[X][Y][option] = depth


    # 상하좌우 이동
    que.append([X - 1, Y, option, depth + 1])
    que.append([X + 1, Y, option, depth + 1])
    que.append([X, Y - 1, option, depth + 1])
    que.append([X, Y + 1, option, depth + 1])
    # 회전
    if option == 0:
        if Y < len(board)-1 and board[X+1][Y+1] != 1:
            que.append([X, Y, 1, depth + 1])
        if Y < len(board)-1 and board[X][Y+1] != 1:
            que.append([X + 1, Y, 1, depth + 1])
        if Y > 0 and board[X+1][Y-1] != 1:
            que.append([X, Y - 1, 1, depth + 1])
        if Y > 0 and board[X][Y-1] != 1:
            que.append([X+1, Y - 1, 1, depth + 1])
    elif option == 1:
        if X < len(board)-1 and board[X+1][Y] != 1:
            que.append([X, Y+1, 0, depth+1])
        if X < len(board)-1 and board[X+1][Y+1] != 1:
            que.append([X, Y, 0, depth+1])
        if X > 0 and board[X-1][Y] != 1:
            que.append([X-1,Y+1,0,depth+1])
        if X > 0 and board[X-1][Y+1] != 1:
            que.append([X-1,Y,0,depth+1])

    while len(que) > 0:
        X, Y, option, depth = que.popleft()
        ret = BFS(board,visited,que,X,Y,option,depth)
    return ret
    

def solution(board):
    que = collections.deque()

    N = len(board)
    global visited
    visited = [[[-1 for _ in range(2)] for _ in range(N)] for _ in range(N)]

    return BFS(board, visited, que, 0, 0, 1, 0)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
