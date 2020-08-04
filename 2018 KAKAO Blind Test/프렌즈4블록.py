from collections import deque

def section(i1,i2,j1,j2):
    global board
    try:
        if i1 < 0 or i2 < 0 or j1 <0 or j2 < 0:
            return False
        if board[i1] == board[i2] == board[j1] == board[j2]:
            return True
    except IndexError:
        return False


def check(i,j):
    pass

def solution(m, n, board):
    Flag = [[False for _ in n] for _ in m]
    for i in range(m):
        for j in range(n):
            check(i,j)

print(solution(5,4,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))