def solution(n):
    dic = [0 for _ in range(n+1)]
    dic[1] = 1
    dic[2] = 2
    # 오른쪽으로 한칸씩 늘어난다고 생각한다
    for i in range(3,n+1):
        dic[i] = (dic[i-1] + dic[i-2]) % 1000000007
    return dic[i]
print(solution(4))