# 1 뽑기

def solution(board, moves):
    answer = 0
    boardSize = len(board)
    box = []

    for row in moves:
        row -= 1
        for col in range(boardSize):
            if board[col][row] != 0:
                box.append(board[col][row])
                board[col][row] = 0
                if len(box) > 1 and box[len(box) - 1] == box[len(box) - 2]:
                    box.pop()
                    box.pop()
                    answer += 2
                break
    return answer




board = []

# 배열의 수
n = int(input())
# push의 수
for _ in range(n):
    board.append(list(map(int, (input().split()))))

moves = list(map(int, input().split()))
print(solution(board, moves))

