TC = int(input())

for case in range(1, TC+1):
    data = []
    cnt = 0
    n = int(input())
    for _ in range(n):
        a, b = map(int,input().split())
        for i in range(len(data)):
            if (a < data[i][0] and data[i][1] < b) or (data[i][0] < a and b < data[i][1]):
                cnt += 1
        data.append((a, b))
    print(f"#{case} {cnt}")