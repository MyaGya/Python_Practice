# 1952 수영장 이용

T = int(input())
def solve(n, myPrice):
    global total_price
    if 11 < n:
        total_price = min(total_price,myPrice)
    else:
        solve(n + 1, myPrice + price[0] * calender[n])
        solve(n + 1, myPrice + price[1])
        solve(n + 3, myPrice + price[2])

for case in range(1,T+1):

    price = list(map(int,input().split()))
    #이용 계획
    calender = list(map(int,input().split()))
    total_price = price[3]
    solve(0, 0)
    print(f"#{case} {total_price}")
