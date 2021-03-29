from collections import defaultdict


def solution(arrows: list):
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    visited = defaultdict(bool)  # (prev_x,prev_y,x,y) 와 (x,y,prev_x,prev_y) 로 저장
    visited_point = defaultdict(bool)
    x, y = 0, 0
    ret = 0
    visited_point[(0,0)] = True
    for arrow in arrows:
        for i in range(2): # 교차상태 고려를 위해 2칸씩 이동
            prev_x, prev_y = x, y
            x += dx[arrow]
            y += dy[arrow]
            if visited[(x, y, prev_x, prev_y)]: # 한번 지나간 경로일 경우 아무것도 하지 않는다
                pass
            else:                               # 지나가지 않은 경로일 경우
                visited[(x, y, prev_x, prev_y)] = True # 경로 추가
                visited[(prev_x, prev_y, x, y)] = True
                if visited_point[(x,y)]:        # 지나가지 않고 방문했었던 경로일 경우
                    ret += 1
                else:                           # 지나가지 않고 방문하지도 않았던 경로일 경우
                    visited_point[(x,y)] = True
    return ret


#print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5,0,3,0]))
