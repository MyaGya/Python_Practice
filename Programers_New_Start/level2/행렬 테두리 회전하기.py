def make_rotation_target(board, x1, y1, x2, y2) -> list:
    x1, x2, y1, y2 = x1 - 1, x2 - 1, y1 - 1, y2 - 1
    expected_move = []

    x = x1
    for y in range(y1, y2 + 1):
        expected_move.append((x, y))

    y = y2
    for x in range(x1 + 1, x2 + 1):
        expected_move.append((x, y))

    x = x2
    for y in range(y2 - 1, y1 - 1, -1):
        expected_move.append((x, y))

    y = y1
    for x in range(x2 - 1, x1 - 1, -1):
        expected_move.append((x, y))

    return expected_move


def move_rotation(board, expected_move):
    number = int
    for i in range(len(expected_move)):
        x, y = expected_move[i][0], expected_move[i][1]
        tmp = board[x][y]
        board[x][y] = number
        number = tmp


def find_rotation_min(board, expected_move):
    return min(map(lambda x: board[x[0]][x[1]], expected_move))


def solution(rows, columns, queries):
    board = [[None for _ in range(columns)] for _ in range(rows)]

    # init
    auto_increment_number = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = auto_increment_number
            auto_increment_number += 1

    answer = []
    for x1, y1, x2, y2 in queries:
        expected_move = make_rotation_target(board, x1, y1, x2, y2)
        move_rotation(board, expected_move)
        answer.append(find_rotation_min(board, expected_move))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
