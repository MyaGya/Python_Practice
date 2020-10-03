ans = int


def dfs(complite, cnt, numbers,visited):
    if cnt == 0:
        global ans
        ans = max(int("".join(numbers)), ans)
        return
    if (*numbers,cnt) in visited:
        return
    visited[(*numbers,cnt)] = True
    for i in range(complite, len(numbers)):
        for j in range(i + 1, len(numbers)):
            # more then big number -> change
            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(i, cnt-1, numbers,visited)
            numbers[i], numbers[j] = numbers[j], numbers[i]


n = int(input())
for test_case in range(1, n + 1):
    ans = 0
    data, cnt = input().split()
    cnt = int(cnt)
    numbers = list(data)
    visited = dict()
    dfs(0, cnt, numbers,visited)
    print(f"#{test_case} {ans}")