'''
def solution(land):
    # init
    pick = [[0 for _ in range(4)] for _ in range(len(land))]
    pick[0] = land[0]
    for i in range(1,len(land)):
        for j in range(4):
            pick[i][j] = max([pick[i-1][k] for k in range(4) if k != j]) + land[i][j]
    pick[0][0] = 0
    print(id(pick[0]))
    print(id(land[0]))

    return max(pick[i])


'''

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][(j+1)%4],land[i-1][(j+2)%4],land[i-1][(j+3)%4])
    return max(land[i])
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))