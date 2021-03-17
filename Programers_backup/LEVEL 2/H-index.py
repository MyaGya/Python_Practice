def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i: # 인용된 횃수가 >= 인용된 논문의 갯수
            return len(citations)-i
    return 0
print(solution([3,0,6,1,5]))