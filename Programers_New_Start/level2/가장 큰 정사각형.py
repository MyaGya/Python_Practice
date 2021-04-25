def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0 or j == 0:
                continue
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

    max_square = max([max(board_row) for board_row in board])
    return max_square ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
