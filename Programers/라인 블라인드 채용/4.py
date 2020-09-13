def solution(maze):
    # 내가 보고있는 방향
    look_value = [[-1,0],[0,1],[-1,0],[0,-1]] # 순서대로 아래 오른 위 왼
    look_head = [0, 1, 2, 3]  # 어느 쪽을 보고있는가, 아래 오른 위 왼

    pos = [0, 0]
    dest = [len(maze) - 1, len(maze) - 1]


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
