def solution(n):
    change = ['1', '2', '4']
    ans = ""
    while n:
        ans += (change[(n - 1) % 3])
        n = (n - 1) // 3
    return ans[::-1]
