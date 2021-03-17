def solution(stones, k):

    # 최초 최솟값
    R = 200000000
    L = 1

    while L <= R:
        mid = (L + R) // 2
        cnt = 0
        for i in range(len(stones)):
            if stones[i]-mid <= 0:
                cnt +=1
            else:
                cnt = 0
            if cnt >= k:
                break;

        if cnt >= k:
            R = mid-1
        else:
            L = mid+1

    return L


k = int(input())
stones = list(map(int, input().split()))

print(solution(stones, k))