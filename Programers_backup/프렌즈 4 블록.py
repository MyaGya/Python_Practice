def solution(m, n, board):
    board = [list(x) for x in board]
    waiting_remove = True # do while
    while waiting_remove:
        waiting_remove = []
        # 1. 2x2 형태를 찾는다
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != '#':
                    waiting_remove.append([i, j])
        # 2. 위치를 #으로 대체한다
        for i, j in waiting_remove:
            board[i][j] = '#'
            board[i + 1][j] = '#'
            board[i][j + 1] = '#'
            board[i + 1][j + 1] = '#'

        # 3. '#' 위치는 그 위에서 '#'이 아닌 수를 찾아 가지고 내려온다
        for _ in range(m):  # 최악의 경우 모든 m이 #일 수 있다
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':  # 밑의 값이 #일 경우
                        board[i + 1][j], board[i][j] = board[i][j], '#'
    return sum([L.count('#') for L in board])

print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))