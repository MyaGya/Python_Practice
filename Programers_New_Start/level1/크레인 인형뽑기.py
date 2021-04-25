def solution(board: list, moves: list):
    root = []
    answer = 0
    for move in moves:
        column = move - 1
        row = 0
        while row < len(board):
            if board[row][column]:
                root.append(board[row][column])
                board[row][column] = 0
                break
            row += 1

        while len(root) > 1 and root[-1] == root[-2]:
            root.pop()
            root.pop()
            answer += 2
    return answer


print(solution(
    [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]], [1, 2, 3, 3, 2, 3, 1]))
