from collections import defaultdict


def find_ractangle(value,rectangle,board): # value의 직사각형의 시작과 끝점을 기준으로 가능한지 아닌지를 판별한다
    L = list(zip(*rectangle[value]))
    y1,y2 = min(L[0]), max(L[0])
    x1,x2 = min(L[1]), max(L[1])
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            if board[i][j] == 0 or board[i][j] != value:
                break
        if board[i][j] == 0 or board[i][j] != value:
            break
    else:
        return True # 사각형을 지울 수 있는 경우
    return False # 사각형을 지울 수 없는 경우


def remove_ractangle(value,ractangle,board):
    possible = [True for _ in range(len(board))]
    re_calc = set() # 제거된 위치
    for L in ractangle[value]:
        board[L[0]][L[1]] = 0
        re_calc.add(L[1])
    re_calc = list(re_calc)

    for i in range(len(board)): # 반복하며 없어진 도형의 위치를 채운다
        for j in re_calc:
            if board[i][j] == -1:
                continue
            else:
                if board[i][j] == 0:
                    if possible[board[i][j]]:
                        board[i][j] = -1
                else:
                    possible[j] = False
def solution(board):
    rectangle = defaultdict(list)  # 지워야 하는 번호의 주소가 담겨있다
    possible = [True for _ in range(len(board))]  # 해당 보드판의 위치가 블럭을 놓을 수 있는가?
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                if possible[j]:    board[i][j] = -1  # 검은색으로 채우기
            else:
                possible[j] = False  # 못가는 공간 채우기
                rectangle[board[i][j]].append([i,j])
    ret = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != (0 or -1):
                if find_ractangle(board[i][j],rectangle,board):
                    remove_ractangle(board[i][j],rectangle,board)
                    ret += 1
    return ret


print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))