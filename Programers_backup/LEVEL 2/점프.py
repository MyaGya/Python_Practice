# idea : 코드 블럭으로 계산

# 10000개의 범위 내에서는 최대 수를 구할 수 있다
visited = [0]*10001
for i in range(1,10000):
    jumpValue = visited[i-1] + 1
    jumpPosition = i
    jump = 2 # 1의 경우에는 i 재귀로 1차적으로 처리하였으므로 2부터 시작
    while jumpPosition < 10001:
        if visited[jumpPosition] == 0:
            visited[jumpPosition] = jumpValue
        jumpPosition += jump
        jump += 1
        jumpValue += 1


n = int(input())

for case in (1,n+1):
    a, b = map(int, input().split())
    i = 1
    prev = 0
    data = []
    # init
    while True:
        now = prev + i
        if a <= now:
            if now <= b:
                data.append([prev, now, i])
            else:
                data.append([prev, now, i])
                break
        prev = now
        i += 1
    print(data)