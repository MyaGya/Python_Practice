# check함수의 경우의 수를 줄여주어야 한다.
# 현재는 n이 12일 경우 12!만큼 계산해야 하므로 시간초과가 발생한다
ret = 0
def solution(n):
    board = [[False for _ in range(n)] for _ in range(n)]


    def check(row ,col):
        for i in range(n):
            if board[row][i]:
                return False
        for i in range(n):
            if board[i][col]:
                return False
        x, y = col - min(row,col), row - min(row,col)
        while x < n and y < n:
            if board[y][x]:
                return False
            x, y = x+1, y+1
        y, x = row - min(row, n-1-col), col + min(row, n-1-col)
        while x >= 0 and y < n:
            if board[y][x]:
                return False
            x, y = x-1, y+1
        return True

    def case(depth):
        if depth == n:
            global ret
            ret += 1
            return
        for i in range(n):
            if check(depth, i):
                board[depth][i] = True
                case(depth + 1)
                board[depth][i] = False
    case(0)
    return ret

print(solution(4))
