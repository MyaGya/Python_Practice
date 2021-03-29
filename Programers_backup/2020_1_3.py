
'''
def solution(key, lock):

    holeCount=0
    M, N = len(key), len(lock)
    #구멍의 갯수 계산
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                holeCount += 1
    largeN = N + M*2
    largeLocker = [[0 for col in range(largeN)] for row in range(largeN)]
    # 배열될 자물쇠의 위치
    for i in range(M,M+N):
        for j in range(M,M+N):
            largeLocker[i][j] = int(lock[i-M][j-M])
    for i in range(largeN):
        print(largeLocker[i])
    for i in range(4):
        if search(key, largeLocker):
            return True
        else
            rotate(key)
    return False


    answer = True
    return answer







M, N = map(int, input().split())
list1 = list()
list2 = list()
for _ in range(M):
    list1.append(list(input().split()))
for _ in range(N):
    list2.append(list(input().split()))
solution(list1, list2)


'''