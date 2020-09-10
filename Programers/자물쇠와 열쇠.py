def solution(key, lock):
    # 1. make ex_lock
    ex_lock = [[0 for _ in range(len(key) * 2 + len(lock))] for _ in range(len(key) * 2 + len(lock))] # 확장 자물쇠
    lock_position = [[len(key),len(key) + len(lock)],[len(key),len(key) + len(lock)]] # 실제 자물쇠 값의 위치
    x,y = lock_position[0][0],lock_position[1][0]
    for i in range(len(key)):
        for j in range(len(key)):
            ex_lock[i+x][j+y] = lock[i][j]
    for i in ex_lock:
        print(i)

    # 2. check lock
    for i in range(4): # 방향 회전을 고려한 반복
        pass


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))

