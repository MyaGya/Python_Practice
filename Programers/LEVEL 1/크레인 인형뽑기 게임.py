def solution(board, moves):
    board = list(map(list, zip(*board)))

    for tmp in board:
        tmp.reverse()
        while tmp[-1] == 0:
            tmp.pop()
    stack = []
    ret = 0
    for move in moves:
        move -= 1  # list started 0
        if board[move]:
            stack.append(board[move][-1])
            board[move].pop()
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                ret += 2
    return ret